from tkinter import *

root = Tk()

#creating a label widget
myLabel1 = Label(root, text = "Hello Chaitra, How are you ?")
myLabel2 = Label(root, text = "Hello Chaitra")

#showing it on screen
myLabel1.grid(row= 0, column = 0)
myLabel2.grid(row = 1, column = 1)


root.mainloop()

