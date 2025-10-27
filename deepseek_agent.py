# deepseek_agent.py - 基础的DeepSeek Agent类
import requests
import json
from config import config

class DeepSeekAgent:
    """基础的DeepSeek API交互类"""
    
    def __init__(self):
        self.api_key = config.api_key
        self.base_url = config.base_url
        self.headers = config.headers
    
    def send_message(self, 
                    message: str, 
                    system_prompt: str = "你是一个有用的助手",
                    model: str = "deepseek-chat",
                    temperature: float = 0.7) -> str:
        """
        发送消息到DeepSeek API并获取回复
        
        参数:
            message: 用户输入的消息
            system_prompt: 系统角色设定
            model: 使用的模型
            temperature: 生成文本的随机性 (0.0-1.0)
        """
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            "temperature": temperature,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"API请求错误: {e}"
        except KeyError:
            return "解析响应时出错"
    
    def chat_with_history(self, messages: list, temperature: float = 0.7) -> str:
        """使用消息历史进行对话"""
        data = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": temperature,
            "stream": False
        }
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            return f"API请求错误: {e}"