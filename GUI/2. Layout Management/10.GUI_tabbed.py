import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)  #create a tab
tabControl.add(tab1,text="Tab 1")   #add the tab
tabControl.pack(expand=1,fill="both")   #pack to make visible
tabControl.add(tab2,text="Tab 2")

win.mainloop()
