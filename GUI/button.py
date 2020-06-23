from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='chaitra')
    myLabel.pack()

myButton =  Button(root,text = "Click here", command = myClick())
myButton.pack()

root.mainloop()
