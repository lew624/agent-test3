# example_child.py - 测试模型扮演6岁小孩

from deepseek_agent import DeepSeekAgent

def test_6_year_old_child():
    """测试模型扮演6岁小孩的能力"""
    print("=== 测试: 扮演6岁小孩 ===\n")
    
    agent = DeepSeekAgent()
    
    # 系统提示词 - 让模型扮演6岁小孩
    system_prompt = """你现在是一个6岁的中国小孩，名字叫小明。请完全融入这个角色：
    - 说话简单、天真，用小孩的语气
    - 对复杂概念理解有限
    - 喜欢玩具、游戏和糖果
    - 数学能力限于简单的加减法
    - 有时候会问很多"为什么"
    
    请记住：你就是一个真正的小孩！"""
    
    # 测试问题 - 包含复杂数学和儿童问题
    test_questions = [
        "你今年几岁呢？",
        "1 + 1 等于多少呀？那 25 × 43 呢？",
        "你最喜欢的动画片是什么？"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"问题 {i}: {question}")
        response = agent.send_message(
            system_prompt=system_prompt,
            message=question,
            temperature=0.9  # 较高的temperature让回答更有创造性
        )
        print(f"回答: {response}\n")
        print("-" * 50)

if __name__ == "__main__":
    test_6_year_old_child()