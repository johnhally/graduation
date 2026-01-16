import json
from datetime import datetime
from typing import List, Dict, Any
from agentic_memory.memory_system import AgenticMemorySystem


class MemoryChatBot:
    def __init__(self, memory_system: AgenticMemorySystem, max_history: int = 10):
        self.memory_system = memory_system
        self.history = []  # 短期对话历史 (Short-term memory)
        self.max_history = max_history  # 限制上下文轮数，防止token溢出

        # 定义机器人的“人设”和指令
        self.system_prompt = """
        You are a personalized AI assistant with access to the user's long-term memory.
        
        Your Goal:
        Answer the user's questions or engage in chat by utilizing the [Relevant Memories] provided below.

        Guidelines:
        1. IF the user asks about past events, preferences, or notes, PRIORTIZE information from [Relevant Memories].
        2. IF [Relevant Memories] contains the answer, explicitly mention that you remember it (e.g., "Based on your notes...", "I recall that...").
        3. IF the information is not in the memories, simply say you don't have that information or answer using general knowledge, but clarify it's general knowledge.
        4. Maintain a helpful, empathetic, and clear tone.
        5. Combine multiple memory fragments to form a coherent answer if needed.
        """

    def _get_time_context(self) -> str:
        """获取当前时间并格式化，用于 Prompt"""
        now = datetime.now()
        weekday = now.strftime("%A")  # 星期几
        date_str = now.strftime("%Y-%m-%d %H:%M")
        return f"Current System Time: {date_str} ({weekday})"

    def _format_memories_for_prompt(self, relevant_memories: List[Dict[str, Any]]) -> str:
        """将检索到的记忆格式化为字符串，嵌入 Prompt"""
        if not relevant_memories:
            return "No relevant past memories found."

        formatted_text = "Found the following relevant memories:\n"
        for i, mem in enumerate(relevant_memories):
            # 你的 search 方法返回包含 content, timestamp, tags 等字段的字典
            formatted_text += (
            f"- MEMORY_ID: {mem['id']}\n"
            f"  TIME: {mem.get('timestamp','Unknown')}\n"
            f"  SCORE: {mem.get('score',0):.3f}\n"
            f"  CONTEXT: {mem.get('context','')}\n"
            f"  CONTENT: {mem.get('content','')}\n"
            f"  TAGS: {', '.join(mem.get('tags',[]))}\n"
        )
            print(formatted_text)

        return formatted_text

    def chat(self, user_input: str) -> str:
        """核心对话循环"""

        # --- 步骤 1: 检索记忆 (RAG Core) ---
        # 简单策略：直接用用户输入去搜索
        # 进阶策略（毕设加分点）：可以使用 LLM 先把 user_input 改写成搜索关键词再搜索
        print(f"🤖 (Searching memories for: '{user_input}')...")
        results = self.memory_system.search(user_input, k=3)  # 检索最相关的3条

        memory_context = self._format_memories_for_prompt(results)
        print(f"🧠 (Retrieved Context):\n{memory_context}")

        # --- 步骤 2: 构建完整的 Prompt ---
        # 结构：系统指令 + 长期记忆上下文 + 短期对话历史 + 当前输入

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": self._get_time_context()}, #😀添加了时序
            {"role": "system", "content": f"[Relevant Memories Retrieved from Database]:\n{memory_context}"}
        ]

        # 添加短期历史 (最近 N 轮)
        messages.extend(self.history[-self.max_history:])

        # 添加当前用户输入
        messages.append({"role": "user", "content": user_input})

        # --- 步骤 3: 调用 LLM 生成回答 ---
        # 复用 memory_system 中的 llm_controller，避免重复写调用逻辑
        # 注意：我们需要直接通过 client 调用 chat completion，或者修改 llm_controller 支持 list 格式的 messages
        # 这里为了演示简单，我们假设你的 LLMController 可以处理 raw prompt 或我们需要稍微适配一下

        # 由于你的 LLMController.get_completion 封装是针对 str prompt 的
        # 我们这里临时手动拼接成 string 传给它，或者最好给 LLMController 加一个 chat 方法
        # 方案 A：拼接 String (简单，但对于 chat 模型效果不如 list 好)
        full_prompt_str = f"{self.system_prompt}\n\n[Relevant Memories]:\n{memory_context}\n\n[Conversation]:\n"
        for msg in self.history[-self.max_history:]:
            full_prompt_str += f"{msg['role']}: {msg['content']}\n"
        full_prompt_str += f"user: {user_input}\nassistant:"

        # 调用生成 (这里假设你不想改底层代码，我们用 get_completion 强行生成，虽然这通常用于单次指令)
        # *更好的做法是去修改 llm_controller.py 增加一个 chat() 方法*
        # 这里演示直接调用 openai client (如果你在 controller 暴露了 client)
        # 或者我们直接使用 get_completion

        response_text = self.memory_system.llm_controller.llm.client.chat.completions.create(
            model=self.memory_system.llm_controller.llm.model,
            messages=messages,
            temperature=0.7
        ).choices[0].message.content

        # --- 步骤 4: 更新短期记忆 ---
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "assistant", "content": response_text})

        return response_text

    def save_current_interaction(self, user_input: str, response: str):
        """
        可选：将刚才的对话也存入长期记忆库
        这样机器人就能记住'它刚才和你说过什么'，实现自我进化的记忆
        """
        # 并不是每句话都值得存，可以加一个判断逻辑，或者直接存
        content_to_save = f"User asked: {user_input}\nAssistant answered: {response}"
        self.memory_system.add_note(content_to_save, tags=["chat_history"])