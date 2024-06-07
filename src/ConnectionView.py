import tkinter as tk
from tkinter import ttk

class ConnectionView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Network Monitor - By Spring-0")
        
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("PID", "Protocol", "Direction", "Source IP", "Source Port", "Target IP", "Target Port")
        self.tree.heading("#0", text="Process Name")
        self.tree.column("#0", width=100)
        
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
            
        self.tree.pack(expand=True, fill="both")