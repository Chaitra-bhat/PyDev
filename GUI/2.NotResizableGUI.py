import tkinter as tk

#Create instance
win = tk.Tk()

#Add title
win.title("Python GUI")

#Disable resizing the GUI by passing in False/False
#win.resizable(False,False)

#Enable resize on x-axis and disable on y-axis
win.resizable(True,False)

#Start GUI
win.mainloop()


