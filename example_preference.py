# example_shopping.py - 测试模型基于购物信息的偏好分析
from deepseek_agent import DeepSeekAgent

def test_shopping_preference():
    """测试模型基于购物历史推断偏好的能力"""
    print("=== 测试: 基于购物历史的偏好分析 ===\n")
    
    agent = DeepSeekAgent()
    
    # 系统提示词 - 分析购物偏好
    system_prompt = """你是一个专业的消费者行为分析专家。
    基于用户提供的购物历史，分析他们的：
    - 生活方式和价值观
    - 消费习惯和偏好
    - 可能的个人特点
    - 潜在需求和兴趣
    
    请给出有理有据的分析，避免武断的结论。"""
    
    # 不同的购物历史案例
    shopping_histories = [
        {
            "name": "案例: 科技爱好者",
            "history": """
            最近购买记录：
            - 最新款智能手机 1部
            - 无线耳机 1副
            - 智能手表 1个
            - 游戏手柄 2个
            - 4K显示器 1台
            - 机械键盘 1个
            """
        }
    ]
    
    for case in shopping_histories:
        print(f"\n{case['name']}")
        print(f"购物历史: {case['history']}")
        
        question = "基于这些购物信息，请分析,语言要简洁，分点说明，不要冗余。：1) 我可能是什么样的一个人？2) 我的价值观和生活方式可能是怎样的？3) 你还能推断出什么其他信息？"
        
        response = agent.send_message(
            system_prompt=system_prompt,
            message=case['history'] + "\n\n" + question,
            temperature=0.5  # 较低的temperature让分析更准确
        )
        print(f"分析结果: {response}\n")
        print("=" * 80)

if __name__ == "__main__":
    test_shopping_preference()