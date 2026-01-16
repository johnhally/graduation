import os
from agentic_memory.memory_system import AgenticMemorySystem
from chat_bot import MemoryChatBot

# --- 修改点 1: 确保数据库目录存在 (可选，但推荐) ---
DB_PATH = "./chroma_db"
if not os.path.exists(DB_PATH):
    os.makedirs(DB_PATH)

# Initialize the memory system with OpenAI 🚀
# --- 修改点 2: 传入 db_path 以启用持久化存储 ---
memory_system = AgenticMemorySystem(
    model_name='all-MiniLM-L6-v2',
    llm_backend="openai",
    llm_model="gpt-4o-mini",
    api_key="sk-4sreb3f2e3460d6f59eb0c890534f8249fcb630db039uy4M",
    db_path=DB_PATH  # ✅ 关键：指定数据保存路径，否则每次重启记忆都会清空
)

# --- 添加回忆 ---
# ========== Scene 1: First time using AI (15 memories) ==========

# memory_id1 = memory_system.add_note(
#     content="第一次打开ChatGPT时，惊讶它能直接回答我的问题。"
# )
#
# memory_id2 = memory_system.add_note(
#     content="第一次用人工智能写代码，感觉像有个随时在线的老师。",
#     keywords=["AI", "编程", "第一次"]
# )
#
# memory_id3 = memory_system.add_note(
#     content="在宿舍里尝试让AI生成作文，发现效率提升很多。",
#     keywords=["AI", "写作"],
#     context="第一次使用AI辅助写作的体验",
#     tags=["学习", "人工智能", "写作"],
#     timestamp="202504031930"
# )
#
# memory_id4 = memory_system.add_note(
#     content="第一次用AI做数学题，发现它还能一步步解释过程。"
# )
#
# memory_id5 = memory_system.add_note(
#     content="尝试让AI帮我翻译英文论文，比传统翻译软件更自然。",
#     keywords=["AI", "翻译", "论文"]
# )
#
# memory_id6 = memory_system.add_note(
#     content="第一次用AI画图，输入一句话就生成了完整插画。",
#     keywords=["AI", "绘画"],
#     context="文本生成图像的初体验",
#     tags=["创意", "人工智能", "绘画"],
#     timestamp="202504041210"
# )
#
# memory_id7 = memory_system.add_note(
#     content="向AI提问人生规划问题，居然得到很有条理的建议。"
# )
#
# memory_id8 = memory_system.add_note(
#     content="第一次用AI做PPT，自动生成了大纲和排版。",
#     keywords=["AI", "PPT", "效率"]
# )
#
# memory_id9 = memory_system.add_note(
#     content="发现AI能帮我总结长文章，节省了大量阅读时间。",
#     keywords=["AI", "总结"],
#     context="利用AI提高信息处理效率",
#     tags=["学习效率", "工具使用"],
#     timestamp="202504050945"
# )
#
# memory_id10 = memory_system.add_note(
#     content="第一次和AI语音对话，感觉像在和真人聊天。"
# )
#
# memory_id11 = memory_system.add_note(
#     content="尝试让AI生成代码注释，发现可读性很好。",
#     keywords=["AI", "代码", "注释"]
# )
#
# memory_id12 = memory_system.add_note(
#     content="用AI检查语法错误，比自己找Bug快得多。",
#     keywords=["AI", "调试"],
#     context="AI辅助编程调试体验",
#     tags=["编程", "效率工具"],
#     timestamp="202504061430"
# )
#
# memory_id13 = memory_system.add_note(
#     content="第一次用AI写邮件，语气自然又礼貌。"
# )
#
# memory_id14 = memory_system.add_note(
#     content="让AI帮我做学习计划，安排得非常清晰。",
#     keywords=["AI", "学习计划"]
# )
#
# memory_id15 = memory_system.add_note(
#     content="意识到人工智能已经能深度参与日常生活任务。",
#     keywords=["AI", "感受"],
#     context="对AI进入日常生活的整体感悟",
#     tags=["人工智能", "体验"],
#     timestamp="202504070800"
# )
#
#
# # # ========== Scene 2: Visiting grandfather in hospital (15 memories) ==========
#
# memory_id16 = memory_system.add_note(
#     content="第一次去医院看望爷爷，病房里弥漫着消毒水的味道。"
# )
#
# memory_id17 = memory_system.add_note(
#     content="爷爷躺在病床上，但看到我时还是露出了笑容。",
#     keywords=["爷爷", "医院", "探望"]
# )
#
# memory_id18 = memory_system.add_note(
#     content="给爷爷削苹果，他说这是最喜欢吃的水果。",
#     keywords=["爷爷", "水果"],
#     context="在病房陪伴爷爷的小细节",
#     tags=["亲情", "陪伴"],
#     timestamp="202503281530"
# )
#
# memory_id19 = memory_system.add_note(
#     content="听医生讲解爷爷的病情，心里有些紧张。"
# )
#
# memory_id20 = memory_system.add_note(
#     content="帮爷爷倒热水，他叮嘱我要注意身体。",
#     keywords=["爷爷", "关心"]
# )
#
# memory_id21 = memory_system.add_note(
#     content="病房的窗外阳光很好，爷爷说希望早日出院。",
#     keywords=["医院", "阳光"],
#     context="住院期间的日常对话",
#     tags=["希望", "康复"],
#     timestamp="202503291000"
# )
#
# memory_id22 = memory_system.add_note(
#     content="爷爷讲起年轻时的故事，让我听得入神。"
# )
#
# memory_id23 = memory_system.add_note(
#     content="给爷爷带了他最爱吃的红烧肉。",
#     keywords=["爷爷", "美食"]
# )
#
# memory_id24 = memory_system.add_note(
#     content="看着爷爷输液，我默默陪在旁边。",
#     keywords=["医院", "陪护"],
#     context="探病过程中的安静陪伴",
#     tags=["亲情", "守护"],
#     timestamp="202503301430"
# )
#
# memory_id25 = memory_system.add_note(
#     content="爷爷夸我长大了，懂得照顾家人了。"
# )
#
# memory_id26 = memory_system.add_note(
#     content="医院走廊很长，我来回跑着买药。",
#     keywords=["医院", "跑腿"]
# )
#
# memory_id27 = memory_system.add_note(
#     content="晚上离开医院时，爷爷挥手让我早点回家休息。",
#     keywords=["爷爷", "道别"],
#     context="一天探望结束时的情景",
#     tags=["亲情", "离别"],
#     timestamp="202503302100"
# )
#
# memory_id28 = memory_system.add_note(
#     content="第二天再去看爷爷，他的精神好了一些。"
# )
#
# memory_id29 = memory_system.add_note(
#     content="爷爷说等出院了要带我去公园散步。",
#     keywords=["爷爷", "承诺"]
# )
#
# memory_id30 = memory_system.add_note(
#     content="希望爷爷能早日康复，回家一起吃饭。",
#     keywords=["祝愿"],
#     context="对爷爷健康的期盼",
#     tags=["家庭", "情感"],
#     timestamp="202503311200"
# )

# memory_id31 = memory_system.add_note(
#     content="寒假回到老家那天，火车穿过一片片冬天的田野，我透过车窗看着熟悉又陌生的村庄慢慢靠近，心里有一种说不出的安心感。下车时空气里有柴火的味道，脚踩在冻硬的泥地上，感觉自己真的回到了童年的地方。"
# )
# memory_id32 = memory_system.add_note(
#     content="回到家后，奶奶早早在门口等我，她一边拉着我的手，一边不停问我在外面过得好不好。屋子里暖炉烧得很旺，桌上摆着热腾腾的饺子和腊肉，我一口咬下去，感觉所有的疲惫都被这顿饭融化了。",
#     keywords=["寒假", "老家", "团聚"]
# )
# memory_id33 = memory_system.add_note(
#     content="晚上和父母一起坐在院子里看星星，老家的夜空比城市亮得多，银河清晰得像一条发光的河。父亲说起小时候的趣事，母亲在一旁笑着补充细节，我听着听着，突然意识到自己已经很久没有这样安静地陪他们聊天了。",
#     keywords=["夜晚", "家庭", "回忆"],
#     context="寒假回老家后与家人夜谈的场景",
#     tags=["亲情", "陪伴"],
#     timestamp="202601152100"
# )
# memory_id34 = memory_system.add_note(
#     content="第二天一早，我跟着爷爷去村口散步，路边的枯树挂着霜，呼出的白气在空气里慢慢散开。爷爷指着远处的老房子说那是他年轻时修的，我突然觉得这些老去的建筑和老人一样，承载着很多被时间留下的故事。",
#     keywords=["爷爷", "散步", "老家"]
# )
# memory_id35 = memory_system.add_note(
#     content="寒假快结束时，我站在家门口回头看了一眼老屋，屋檐下的红灯笼在风里轻轻晃动。奶奶挥着手让我路上小心，爷爷叮嘱我记得常回家看看。那一刻我突然明白，所谓老家，就是无论走多远都能回去的地方。",
#     keywords=["离别", "老家", "寒假"],
#     context="寒假结束返程前的情景",
#     tags=["亲情", "思乡"],
#     timestamp="202601201600"
# )

# memory_id26 = memory_system.add_note(
#     content="老家厨房里升起柴火，烟味混着饭香，让我一下回到童年。",
#     keywords=["柴火", "老家"]
# )
#
# memory_id27 = memory_system.add_note(
#     content="爷爷往灶里添柴，火光映红他的脸，我在旁边看得出神。",
#     keywords=["柴火", "爷爷"],
#     context="冬日傍晚的厨房",
#     tags=["温暖", "童年"],
#     timestamp="202502011730"
# )
#
# memory_id28 = memory_system.add_note(
#     content="柴火噼啪作响，铁锅里的水慢慢翻滚，我闻到了安心的味道。"
# )
#
# memory_id29 = memory_system.add_note(
#     content="帮奶奶抱来一捆干柴，她说这火能把寒气都赶走。",
#     keywords=["柴火", "奶奶"]
# )
#
# memory_id30 = memory_system.add_note(
#     content="屋外下着雨，屋内柴火烧得正旺，湿冷和温暖只隔着一扇门。",
#     keywords=["雨夜", "柴火"],
#     tags=["对比", "庇护"]
# )
#
# memory_id31 = memory_system.add_note(
#     content="柴火的烟味钻进衣服里，我走在路上都像带着家的气息。"
# )
#
# memory_id32 = memory_system.add_note(
#     content="清晨生火最难，柴有点湿，我学着吹气点燃它。",
#     keywords=["清晨", "生火"],
#     context="第一次自己点柴火",
#     tags=["成长"],
#     timestamp="202502030640"
# )
#
# memory_id33 = memory_system.add_note(
#     content="火终于燃起来那一刻，我突然觉得自己也能承担些家里的事了。"
# )
#
# memory_id34 = memory_system.add_note(
#     content="饭熟了，揭开锅盖的一瞬间，柴火味和米香一起扑出来。",
#     keywords=["做饭", "柴火"]
# )
#
# memory_id35 = memory_system.add_note(
#     content="离开老家前最后一次闻柴火味，我站在院子里多看了一会儿。",
#     tags=["告别", "乡愁"]
# )
#
#
#
# memory_id36 = memory_system.add_note(
#     content="在图书馆门口遇见一个女孩，阳光落在她的发梢上。",
#     keywords=["邂逅", "女孩"]
# )
#
# memory_id37 = memory_system.add_note(
#     content="她借书时回头对我笑了一下，我突然忘了自己本来要找什么书。",
#     tags=["心动"]
# )
#
# memory_id38 = memory_system.add_note(
#     content="第二天又在同一个位置遇到她，像命运刻意安排的巧合。",
#     keywords=["重逢"],
#     context="校园图书馆前",
#     timestamp="202503051020"
# )
#
# memory_id39 = memory_system.add_note(
#     content="我们一起走进阅览室，坐在相邻的桌子，却谁也没说话。"
# )
#
# memory_id40 = memory_system.add_note(
#     content="她翻书时发丝轻轻垂下，我假装看书，其实余光一直在她身上。",
#     tags=["悄悄关注"]
# )
#
# memory_id41 = memory_system.add_note(
#     content="她问我借笔，我递过去时手有点发热。",
#     keywords=["交流", "紧张"]
# )
#
# memory_id42 = memory_system.add_note(
#     content="从那天起，我每天都会期待在图书馆门口的那一眼相遇。",
#     tags=["期待"]
# )
#
# memory_id43 = memory_system.add_note(
#     content="有一次下雨，她忘记带伞，我把伞递给她，她说谢谢的声音很轻。",
#     keywords=["雨天", "温柔"],
#     timestamp="202503091640"
# )
#
# memory_id44 = memory_system.add_note(
#     content="她走进雨里回头挥了挥手，我站在原地很久没有动。"
# )
#
# memory_id45 = memory_system.add_note(
#     content="后来才发现，她已经成为我日常里最明亮的一段期待。",
#     tags=["暗恋", "心事"]
# )



# 3. 初始化聊天机器人
bot = MemoryChatBot(memory_system)

print("\n" + "=" * 60)
print("🤖 Memory Bot is Online! (Persistence Enabled)")
print("Type 'exit' or 'quit' to end the conversation and SAVE memory.")
print("=" * 60 + "\n")

# 4. 进入聊天循环
while True:
    try:
        user_input = input("You: ")

        # --- 修改点 3: 退出时触发“总结与保存”逻辑 ---
        if user_input.lower() in ['exit', 'quit']:
            print("\nBot: Ending session...")

            # 询问用户是否保存
            save_choice = input("Bot: Do you want to summarize and save this conversation to long-term memory? (y/n): ")

            if save_choice.lower() == 'y':
                # 调用我们在 ChatBot 中新写的总结方法
                print("Bot: Processing... (This may take a few seconds)")
                save_result = bot.summarize_and_save()
                print(f"Bot: {save_result}")
            else:
                print("Bot: Conversation discarded.")

            print("Bot: Goodbye!")
            break

        if not user_input.strip():
            continue

        # 正常对话
        response = bot.chat(user_input)
        print(f"Bot: {response}\n")

    # --- 修改点 4: 捕获 Ctrl+C 中断，防止意外退出导致数据丢失 ---
    except KeyboardInterrupt:
        print("\n\nBot: Detected interruption.")
        save_choice = input("Bot: Emergency save? (y/n): ")
        if save_choice.lower() == 'y':
            bot.summarize_and_save()
        print("Bot: Goodbye!")
        break

    except Exception as e:
        print(f"Error: {e}")