import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#Add a title
win.title("Python GUI")

#Adding a label
ttk.Label(win, text = "A label to the world biigest creature in humans as well").grid(column=0,row=0)

#resizing
#win.resizable(False,False)

#Start GUI
win.mainloop()

          
