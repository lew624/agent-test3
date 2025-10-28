from typing import List
import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)

class FamilyMember:
    def __init__(self, name: str, role: str, stance: str, personality: str):
        self.name = name
        self.role = role
        self.stance = stance
        self.personality = personality

    def speak(self, context: List[str]) -> str:
        messages = [
            {"role": "system", "content": f"你是{self.role}，名字叫{self.name}。你对是否给7岁孙子报补习班的立场是：{self.stance}。你的性格是：{self.personality}。请用第一人称，简短地表达你的观点，不要重复别人说过的内容。"},
            {"role": "user", "content": "\n".join(context[-5:])}
        ]
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.8
        )
        return response.choices[0].message.content.strip()