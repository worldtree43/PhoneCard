import tkinter as tk
from column_selection import ColumnSelectionApp

def main():
    root = tk.Tk()
    app = ColumnSelectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
