from typing import List
from agents import FamilyMember

class Debate:
    def __init__(self, members: List[FamilyMember], topic: str, rounds: int = 3):
        self.members = members
        self.topic = topic
        self.rounds = rounds
        self.context = [f"主持人：今天我们要讨论的话题是：{topic}"]

    def start(self):
        for i in range(self.rounds):
            print(f"\n--- 第 {i+1} 轮发言 ---")
            for member in self.members:
                try:
                    speech = member.speak(self.context)
                    print(f"{member.name}（{member.role}）：{speech}")
                    self.context.append(f"{member.name}：{speech}")
                except Exception as e:
                    print(f"{member.name} 发言失败：{e}")