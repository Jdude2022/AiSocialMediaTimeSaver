from ast import main
from tkinter import *
from tkinter import ttk

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