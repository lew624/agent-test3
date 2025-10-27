# config.py - API密钥和基础配置
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置类，用于管理API密钥和其他设置"""
    
    def __init__(self):
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        if not self.api_key:
            raise ValueError("请在.env文件中设置DEEPSEEK_API_KEY环境变量")
        
        self.base_url = "https://api.deepseek.com/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
    
    def get_config(self):
        """返回配置字典"""
        return {
            "api_key": self.api_key,
            "base_url": self.base_url,
            "headers": self.headers
        }

# 创建全局配置实例
config = Config()