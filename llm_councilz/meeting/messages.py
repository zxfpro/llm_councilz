from typing import List, Dict, Any

class MeetingMessageHistory:
    def __init__(self):
        self._messages: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: str, speaker_name: str = None):
        """添加一条消息到历史记录。"""
        message = {"role": role, "content": content}
        if speaker_name:
            message["speaker"] = speaker_name # 添加发言者元信息
        self._messages.append(message)

    def get_messages(self) -> List[Dict[str, Any]]:
        """获取当前完整的消息历史。"""
        return self._messages

    def clear(self):
        """清空消息历史。"""
        self._messages = []

    def __str__(self) -> str:
         return "\n".join([f"[{msg.get('speaker', msg['role'])}] {msg['content']}" for msg in self._messages])
    
    