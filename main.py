import tkinter as tk
from modules.app_with_view import AppWithView

if __name__ == "__main__":
    root = tk.Tk()
    app = AppWithView(root)
    root.mainloop()