from openai import api_key

from agentic_memory.memory_system import AgenticMemorySystem
from chat_agent import MemoryChatBot

# Initialize the memory system with OpenAI 🚀
memory_system = AgenticMemorySystem(
    model_name='all-MiniLM-L6-v2',  # Embedding model for ChromaDB
    llm_backend="openai",           # LLM backend (openai/ollama/sglang/openrouter)
    llm_model="gpt-4o-mini",         # LLM model name
    api_key = "sk-4sreb3f2e3460d6f59eb0c890534f8249fcb630db039uy4M"
)

# ========== Scene 1: First time using AI (15 memories) ==========

memory_id1 = memory_system.add_note(
    content="I第一次打开ChatGPT时，惊讶它能直接回答我的问题。"
)

memory_id2 = memory_system.add_note(
    content="第一次用人工智能写代码，感觉像有个随时在线的老师。",
    keywords=["AI", "编程", "第一次"]
)

memory_id3 = memory_system.add_note(
    content="在宿舍里尝试让AI生成作文，发现效率提升很多。",
    keywords=["AI", "写作"],
    context="第一次使用AI辅助写作的体验",
    tags=["学习", "人工智能", "写作"],
    timestamp="202504031930"
)

memory_id4 = memory_system.add_note(
    content="第一次用AI做数学题，发现它还能一步步解释过程。"
)

memory_id5 = memory_system.add_note(
    content="尝试让AI帮我翻译英文论文，比传统翻译软件更自然。",
    keywords=["AI", "翻译", "论文"]
)

memory_id6 = memory_system.add_note(
    content="第一次用AI画图，输入一句话就生成了完整插画。",
    keywords=["AI", "绘画"],
    context="文本生成图像的初体验",
    tags=["创意", "人工智能", "绘画"],
    timestamp="202504041210"
)

memory_id7 = memory_system.add_note(
    content="向AI提问人生规划问题，居然得到很有条理的建议。"
)

memory_id8 = memory_system.add_note(
    content="第一次用AI做PPT，自动生成了大纲和排版。",
    keywords=["AI", "PPT", "效率"]
)

memory_id9 = memory_system.add_note(
    content="发现AI能帮我总结长文章，节省了大量阅读时间。",
    keywords=["AI", "总结"],
    context="利用AI提高信息处理效率",
    tags=["学习效率", "工具使用"],
    timestamp="202504050945"
)

memory_id10 = memory_system.add_note(
    content="第一次和AI语音对话，感觉像在和真人聊天。"
)

memory_id11 = memory_system.add_note(
    content="尝试让AI生成代码注释，发现可读性很好。",
    keywords=["AI", "代码", "注释"]
)

memory_id12 = memory_system.add_note(
    content="用AI检查语法错误，比自己找Bug快得多。",
    keywords=["AI", "调试"],
    context="AI辅助编程调试体验",
    tags=["编程", "效率工具"],
    timestamp="202504061430"
)

memory_id13 = memory_system.add_note(
    content="第一次用AI写邮件，语气自然又礼貌。"
)

memory_id14 = memory_system.add_note(
    content="让AI帮我做学习计划，安排得非常清晰。",
    keywords=["AI", "学习计划"]
)

memory_id15 = memory_system.add_note(
    content="意识到人工智能已经能深度参与日常生活任务。",
    keywords=["AI", "感受"],
    context="对AI进入日常生活的整体感悟",
    tags=["人工智能", "体验"],
    timestamp="202504070800"
)


# ========== Scene 2: Visiting grandfather in hospital (15 memories) ==========

memory_id16 = memory_system.add_note(
    content="第一次去医院看望爷爷，病房里弥漫着消毒水的味道。"
)

memory_id17 = memory_system.add_note(
    content="爷爷躺在病床上，但看到我时还是露出了笑容。",
    keywords=["爷爷", "医院", "探望"]
)

memory_id18 = memory_system.add_note(
    content="给爷爷削苹果，他说这是最喜欢吃的水果。",
    keywords=["爷爷", "水果"],
    context="在病房陪伴爷爷的小细节",
    tags=["亲情", "陪伴"],
    timestamp="202503281530"
)

memory_id19 = memory_system.add_note(
    content="听医生讲解爷爷的病情，心里有些紧张。"
)

memory_id20 = memory_system.add_note(
    content="帮爷爷倒热水，他叮嘱我要注意身体。",
    keywords=["爷爷", "关心"]
)

memory_id21 = memory_system.add_note(
    content="病房的窗外阳光很好，爷爷说希望早日出院。",
    keywords=["医院", "阳光"],
    context="住院期间的日常对话",
    tags=["希望", "康复"],
    timestamp="202503291000"
)

memory_id22 = memory_system.add_note(
    content="爷爷讲起年轻时的故事，让我听得入神。"
)

memory_id23 = memory_system.add_note(
    content="给爷爷带了他最爱吃的红烧肉。",
    keywords=["爷爷", "美食"]
)

memory_id24 = memory_system.add_note(
    content="看着爷爷输液，我默默陪在旁边。",
    keywords=["医院", "陪护"],
    context="探病过程中的安静陪伴",
    tags=["亲情", "守护"],
    timestamp="202503301430"
)

memory_id25 = memory_system.add_note(
    content="爷爷夸我长大了，懂得照顾家人了。"
)

memory_id26 = memory_system.add_note(
    content="医院走廊很长，我来回跑着买药。",
    keywords=["医院", "跑腿"]
)

memory_id27 = memory_system.add_note(
    content="晚上离开医院时，爷爷挥手让我早点回家休息。",
    keywords=["爷爷", "道别"],
    context="一天探望结束时的情景",
    tags=["亲情", "离别"],
    timestamp="202503302100"
)

memory_id28 = memory_system.add_note(
    content="第二天再去看爷爷，他的精神好了一些。"
)

memory_id29 = memory_system.add_note(
    content="爷爷说等出院了要带我去公园散步。",
    keywords=["爷爷", "承诺"]
)

memory_id30 = memory_system.add_note(
    content="希望爷爷能早日康复，回家一起吃饭。",
    keywords=["祝愿"],
    context="对爷爷健康的期盼",
    tags=["家庭", "情感"],
    timestamp="202503311200"
)


# ========== Search Query Prompts ==========

search_prompt_ai = "第一次使用人工智能的经历与体验"
search_prompt_hospital_1 = "去医院看望爷爷的探病回忆"
search_prompt_hospital_2 = "爷爷最喜欢吃什么？"

# 3. 初始化聊天机器人
bot = MemoryChatBot(memory_system)

print("\n" + "=" * 50)
print("🤖 Memory Bot is Online! (Type 'exit' to quit)")
print("Try asking: 'What is my project about?' or 'Do I have any meetings?'")
print("=" * 50 + "\n")

# 4. 进入聊天循环
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Goodbye!")
        break

    if not user_input.strip():
        continue

    try:
        response = bot.chat(user_input)
        print(f"Bot: {response}\n")

        # 可选：如果你希望机器人记住这次对话
        # bot.save_current_interaction(user_input, response)

    except Exception as e:
        print(f"Error: {e}")




###

# # Enhanced Retrieval with Metadata 🔍
# # The system now uses generated metadata for better semantic search
# results = memory_system.search("artificial intelligence data processing", k=3)
# for result in results:
#     print(f"ID: {result['id']}")
#     print(f"Content: {result['content']}")
#     print(f"Context: {result['context']}")
#     print(f"Keywords: {result['keywords']}")
#     print(f"Tags: {result['tags']}")
#     print(f"Relevance Score: {result.get('score', 'N/A')}")
#     print("---")
#
#
# # Update Memories 🔄
# memory_system.update(memory_id1, content="Updated: Deep learning neural networks for pattern recognition")
#
# # Delete Memories ❌
# memory_system.delete(memory_id3)
#
# # Memory Evolution 🧬
# # The system automatically evolves memories by:
# # 1. Using LLM to analyze content and generate semantic metadata
# # 2. Finding relationships using enhanced ChromaDB embeddings (content + metadata)
# # 3. Updating tags, context, and connections based on related memories
# # 4. Creating semantic links between memories
# # This happens automatically when adding or updating memories!