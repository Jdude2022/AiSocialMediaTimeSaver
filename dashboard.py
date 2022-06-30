from ctypes import util
import utils.source_list
from tkinter import *
from tkinter import ttk


class Dashboard:

    def __init__(self, root):

        root.title("Dashboard")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text='Select Source:').grid(column=0, row=0)
        ttk.Combobox(mainframe).grid(column=1,row=0)

        
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)
        '''
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        '''

        # feet_entry.focus()
        root.bind("<Return>", self.calculate)
    
    '''
    def add_combobox(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
    '''
    def calculate(self, *args):  # Note to self, *args is so that the enter key works
        utils.source_list.sources.source_1()


root = Tk()
Dashboard(root)
root.mainloop()