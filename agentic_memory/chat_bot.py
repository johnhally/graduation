import json
from datetime import datetime
from typing import List, Dict, Any, Optional
from agentic_memory.memory_system import AgenticMemorySystem
import logging

logger = logging.getLogger(__name__)


class MemoryChatBot:
    def __init__(self, memory_system: AgenticMemorySystem, max_history: int = 10):
        self.memory_system = memory_system
        self.history = []  # 短期对话历史 (Short-term memory)
        self.max_history = max_history  # 限制上下文轮数，防止token溢出

        # 优化后的 System Prompt：明确区分长期记忆和短期历史
        self.system_prompt = """
        You are a personalized AI assistant with access to the user's Long-Term Memory and Short-Term Context.

        [SOURCES OF INFORMATION]
        1. **Long-Term Memories**: Provided below. Use this for questions about past events, long-term preferences, or stored notes.
        2. **Short-Term Chat History**: The recent messages in this conversation. Use this for follow-up questions or context within the current session.

        [GUIDELINES]
        - IF the user asks about the past, PRIORTIZE [Long-Term Memories].
        - IF the user refers to something said just a moment ago, use [Short-Term Chat History].
        - IF [Long-Term Memories] contains the answer, explicitly mention it (e.g., "Based on your notes...", "I remember that...").
        - If the answer is not in memory, answer using general knowledge but clarify it is general knowledge.
        - Maintain a helpful, empathetic, and clear tone.
        """

    def _get_time_context(self) -> str:
        """获取当前时间并格式化"""
        now = datetime.now()
        weekday = now.strftime("%A")
        date_str = now.strftime("%Y-%m-%d %H:%M")
        return f"Current System Time: {date_str} ({weekday})"

    def _format_memories_for_prompt(self, relevant_memories: List[Dict[str, Any]]) -> str:
        """将检索到的记忆格式化为字符串"""
        if not relevant_memories:
            return "No relevant past memories found."

        formatted_text = ""
        for i, mem in enumerate(relevant_memories):
            # 格式化每条记忆，只保留核心信息供 LLM 阅读
            tags_str = ", ".join(mem.get('tags', []))
            formatted_text += (
                f"--- Memory {i + 1} ---\n"
                f"Time: {mem.get('timestamp', 'Unknown')}\n"
                f"Content: {mem.get('content', '')}\n"
                f"Tags: [{tags_str}]\n"
            )
        return formatted_text

    def chat(self, user_input: str) -> str:
        """核心对话循环"""

        # --- 步骤 1: 检索长期记忆 ---
        print(f"🤖 (Searching memories for: '{user_input[:20]}...')...")
        results = self.memory_system.search(user_input, k=30)
        memory_context = self._format_memories_for_prompt(results)

        # --- 步骤 2: 构建 Prompt ---
        # 结构：系统指令 + 时间 + 长期记忆 + 短期历史 + 当前输入
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": self._get_time_context()},
            {"role": "system", "content": f"[Relevant Long-Term Memories Retrieved]:\n{memory_context}"}
        ]

        # 关键：将短期历史加入 messages，确保 LLM 能“记住”刚才说的话
        # 我们截取最近的 N 轮对话
        messages.extend(self.history[-self.max_history:])

        # 加入当前用户输入
        messages.append({"role": "user", "content": user_input})

        # --- 步骤 3: 调用 LLM ---
        try:
            # 直接使用 memory_system 中已经初始化好的 client
            response = self.memory_system.llm_controller.llm.client.chat.completions.create(
                model=self.memory_system.llm_controller.llm.model,
                messages=messages,
                temperature=0.7
            )
            response_text = response.choices[0].message.content

            # --- 步骤 4: 更新短期记忆 ---
            self.history.append({"role": "user", "content": user_input})
            self.history.append({"role": "assistant", "content": response_text})

            return response_text

        except Exception as e:
            logger.error(f"Chat generation error: {e}")
            return "Sorry, I encountered an error processing your request."

    def summarize_and_save(self) -> str:
        """
        [新功能] 会话结束时调用。
        让 LLM 总结此次对话的核心信息（忽略废话），并将总结存入长期记忆库。
        """
        if not self.history:
            return "No conversation to save."

        print("🧠 Summarizing session for long-term storage...")

        # 1. 将短期历史拼接成文本
        conversation_str = ""
        for msg in self.history:
            role = "User" if msg['role'] == "user" else "AI"
            conversation_str += f"{role}: {msg['content']}\n"

        # 2. 构建总结专用的 Prompt
        summary_prompt = f"""
        Analyze the following conversation session between a User and an AI.

        Task:
        Extract key facts, user preferences, specific events, or important plans.
        Transform them into a concise, 3rd-person factual memory note.

        Rules:
        - IGNORE casual greetings (hello, how are you), small talk, or system errors.
        - IGNORE questions the user asked that don't reveal information about them.
        - IF the conversation was purely chit-chat with no useful info, return exactly: "NOTHING_TO_SAVE".

        Conversation:
        {conversation_str}

        Memory Note:
        """

        # 3. 调用 LLM 生成总结
        # 这里复用 get_completion (假设它处理单次 prompt)
        summary = self.memory_system.llm_controller.get_completion(summary_prompt)

        # 4. 判断是否需要保存
        if "NOTHING_TO_SAVE" in summary or len(summary.strip()) < 5:
            return "Session ended. No significant information worth saving."

        # 5. 存入长期记忆库
        # 注意：这里调用 add_note 会自动触发你的【记忆演化】逻辑（生成标签、链接邻居）
        # 这就是为什么不需要额外的数据库，add_note 会处理好一切
        new_id = self.memory_system.add_note(
            content=f"Chat Summary ({datetime.now().strftime('%Y-%m-%d')}): {summary}",
            tags=["chat_summary", "conversation"]  # 给个基础标签，系统会自动扩充
        )

        return f"✅ Conversation summarized and saved! (Memory ID: {new_id})\nSummary Content: {summary}"