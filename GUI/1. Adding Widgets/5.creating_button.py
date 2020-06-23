import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#Add a title
win.title("Python GUI")

#Adding a label
a_label = ttk.Label(win,text="A label")
a_label.grid(column=0, row=0)

#Button click
def click_me():
    action.configure(text = "** I have been Clicked!**")
    a_label.configure(foreground = 'red')
    a_label.configure(text='A Red Label')

#Adding a button
action = ttk.Button(win,text="Click Me!",command = click_me)
action.grid(column=1,row=0)

#Start GUI
win.mainloop()

          
