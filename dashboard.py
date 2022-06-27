from ast import main
import tkinter as tk
from tkinter import ttk
'''
def add_source():
    ttk.Combobox(mainframe).grid(column=1, sticky=W)

root = Tk()
root.title('Dashboard')
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row= 0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Label(mainframe, text='Dashboard').grid(column=2, row=0, sticky=N)
ttk.Label(mainframe, text='Sources').grid(column=1, row=1, sticky=W)
ttk.Combobox(mainframe).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text='+', command=add_source).grid(column=2, row=2)
ttk.Button(mainframe, text='Generate').grid(column=3, sticky=(S, W))

root.mainloop()
'''
import random

class DynamicGrid(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.text = tk.Text(self, wrap="char", borderwidth=0, highlightthickness=0,
                            state="disabled")
        self.text.pack(fill="both", expand=True)
        self.boxes = []

    def add_box(self, color=None):
        bg = color if color else random.choice(("red", "orange", "green", "blue", "violet"))
        box = tk.Frame(self.text, bd=1, relief="sunken", background=bg,
                       width=100, height=100)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")

class Example(object):
    def __init__(self):
        self.root = tk.Tk()
        self.dg = DynamicGrid(self.root, width=500, height=200)
        add_button  = tk.Button(self.root, text="Add", command=self.dg.add_box)

        add_button.pack()
        self.dg.pack(side="top", fill="both", expand=True)

        # add a few boxes to start
        for i in range(10):
            self.dg.add_box()

    def start(self):
        self.root.mainloop()

Example().start()