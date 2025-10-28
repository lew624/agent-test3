from agents import FamilyMember
from debate import Debate

# 定义家庭成员
members = [
    FamilyMember("爷爷", "爷爷", "反对", "传统、固执、心疼孙子"),
    FamilyMember("奶奶", "奶奶", "支持", "焦虑、跟风、望孙成龙"),
    FamilyMember("爸爸", "爸爸", "中立", "理性、务实、尊重孩子兴趣"),
    FamilyMember("妈妈", "妈妈", "支持", "焦虑、职场精英、计划性强"),
    FamilyMember("小孩", "7岁孙子", "反对", "天真、爱玩、讨厌作业"),
]

# 启动辩论
debate = Debate(
    members=members,
    topic="是否要给7岁的小孩报补习班？",
    rounds=3
)

debate.start()