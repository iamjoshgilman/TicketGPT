from ttkthemes import ThemedTk
from tkinter import ttk

root = ThemedTk(theme="equilux")
style = ttk.Style(root)
print(style.lookup("TLabel", "foreground"))  # 'TLabel' is the style used for ttk.Label
