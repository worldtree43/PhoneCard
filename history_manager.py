import json
from pathlib import Path

class HistoryManager:
    def __init__(self, file_path='contact_summary.json'):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text('[]')  # 初始化为空列表的 JSON 文件

    def load_history(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_history(self, summary):
        history = self.load_history()
        history.append(summary)
        with open(self.file_path, 'w') as file:
            json.dump(history, file, indent=4)

    def get_history(self):
        return self.load_history()
