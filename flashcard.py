import pandas as pd
import tkinter as tk
from tkinter import simpledialog, messagebox
from history_manager import HistoryManager

class FlashcardApp:
    def __init__(self, master, df, name_col, phone_col, return_callback):
        self.master = master
        self.df = df
        self.name_col = name_col
        self.phone_col = phone_col
        self.return_callback = return_callback
        self.index = 0
        self.results = []
        self.history_manager = HistoryManager()

        self.label = tk.Label(master, text="", font=('Helvetica', 18))
        self.label.pack(pady=20)

        self.success_button = tk.Button(master, text="联系成功", command=self.contact_success)
        self.success_button.pack(side=tk.LEFT, padx=20)

        self.fail_button = tk.Button(master, text="联系失败", command=self.contact_fail)
        self.fail_button.pack(side=tk.LEFT, padx=20)

        self.retry_button = None

        self.show_next_contact()

    def show_next_contact(self):
        if self.index < len(self.df):
            contact = self.df.iloc[self.index]
            self.label.config(text=f"联系人: {contact[self.name_col]}\n电话: {contact[self.phone_col]}")
        else:
            self.show_summary()

    def contact_success(self):
        self.record_result("成功")
        self.show_next_contact()

    def contact_fail(self):
        annotation = simpledialog.askstring("注释", "请输入注释:")
        self.record_result("失败", annotation)
        self.show_next_contact()

    def record_result(self, result, annotation=""):
        record = {
            self.name_col: self.df.iloc[self.index][self.name_col],
            self.phone_col: self.df.iloc[self.index][self.phone_col],
            "Result": result,
            "Annotation": annotation
        }
        self.results.append(record)
        self.index += 1

    def show_summary(self):
        total_contacts = len(self.results)
        successful_contacts = len([res for res in self.results if res['Result'] == "成功"])
        failed_contacts = [res for res in self.results if res['Result'] == "失败"]

        summary = {
            "Total Contacts": total_contacts,
            "Successful Contacts": successful_contacts,
            "Failed Contacts": failed_contacts
        }

        summary_text = (
            f"总共联系了 {total_contacts} 家\n"
            f"联系成功: {successful_contacts} 家\n"
            f"联系失败: {len(failed_contacts)} 家\n"
        )

        if failed_contacts:
            summary_text += "\n失败的联系人:\n"
            for contact in failed_contacts:
                summary_text += f"联系人: {contact[self.name_col]}, 电话: {contact[self.phone_col]}, 注释: {contact['Annotation']}\n"

        self.label.config(text=summary_text)
        self.success_button.pack_forget()
        self.fail_button.pack_forget()

        self.history_manager.save_history(summary)

        if failed_contacts:
            self.retry_button = tk.Button(self.master, text="重试失败的联系人", command=self.retry_failed_contacts)
            self.retry_button.pack(pady=10)

        self.return_button = tk.Button(self.master, text="返回主菜单", command=self.return_to_menu)
        self.return_button.pack(pady=10)

    def retry_failed_contacts(self):
        failed_contacts_df = pd.DataFrame([res for res in self.results if res['Result'] == "失败"])
        self.df = failed_contacts_df[[self.name_col, self.phone_col, 'Annotation']].copy()
        self.index = 0
        self.results = []
        if self.retry_button:
            self.retry_button.pack_forget()
        if self.return_button:
            self.return_button.pack_forget()
        self.success_button.pack(side=tk.LEFT, padx=20)
        self.fail_button.pack(side=tk.LEFT, padx=20)
        self.show_next_contact()

    def return_to_menu(self):
        self.master.destroy()
        self.return_callback()
