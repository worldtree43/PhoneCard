import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from flashcard import FlashcardApp
from history_manager import HistoryManager

class ColumnSelectionApp:
    def __init__(self, master):
        self.master = master
        self.df = None
        self.name_col = tk.StringVar()
        self.phone_col = tk.StringVar()
        self.history_manager = HistoryManager()

        self.label = tk.Label(master, text="欢迎使用PhoneCard", font=('Helvetica', 18))
        self.label.pack(pady=20)

        self.load_file_button = tk.Button(master, text="选择文件", command=self.load_file)
        self.load_file_button.pack(pady=10)

        self.history_button = tk.Button(master, text="查看历史记录", command=self.show_history)
        self.history_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.df = pd.read_excel(file_path)
            self.show_column_selection()

    def show_column_selection(self):
        self.load_file_button.pack_forget()
        self.history_button.pack_forget()
        self.label.pack_forget()

        self.columns = self.df.columns

        # 设置默认选项
        if len(self.columns) > 1:
            self.name_col.set(self.columns[0])
            self.phone_col.set(self.columns[1])

        self.label = tk.Label(self.master, text="请选择联系人和电话的列", font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.name_label = tk.Label(self.master, text="联系人列:")
        self.name_label.pack()
        self.name_dropdown = tk.OptionMenu(self.master, self.name_col, *self.columns)
        self.name_dropdown.pack()

        self.phone_label = tk.Label(self.master, text="电话列:")
        self.phone_label.pack()
        self.phone_dropdown = tk.OptionMenu(self.master, self.phone_col, *self.columns)
        self.phone_dropdown.pack()

        self.submit_button = tk.Button(self.master, text="提交", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        if not self.name_col.get() or not self.phone_col.get():
            messagebox.showerror("错误", "请选择两个列")
        else:
            self.master.destroy()
            root = tk.Tk()
            app = FlashcardApp(root, self.df, self.name_col.get(), self.phone_col.get(), self.return_to_menu)
            root.mainloop()

    def show_history(self):
        history = self.history_manager.get_history()
        if history:
            history_text = "历史记录:\n"
            for summary in history:
                history_text += (
                    f"总共联系了 {summary['Total Contacts']} 家\n"
                    f"联系成功: {summary['Successful Contacts']} 家\n"
                    f"联系失败: {summary['Failed Contacts']} 家\n\n"
                )
            messagebox.showinfo("历史记录", history_text)
        else:
            messagebox.showinfo("历史记录", "没有历史记录")

    def return_to_menu(self):
        root = tk.Tk()
        app = ColumnSelectionApp(root)
        root.mainloop()
