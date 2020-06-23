import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#Add a title
win.title("Chaitra's Calculator")

# addition function on button click
def add_me():
    ans = num1.get() + num2.get()
    action.configure(text='Answer is : ' + str(ans))
    
#Changing label
ttk.Label(win,text="Enter the first number     ").grid(column=0,row=0)
ttk.Label(win,text="Enter the second number ").grid(column=1,row=0)

#Adding a Number Box Entry widget
num1 = tk.IntVar()
num1_entered = ttk.Entry(win,width=12,textvariable=num1)
num1_entered.grid(column=0,row=1)

num2 = tk.IntVar()
num2_entered = ttk.Entry(win,width=12,textvariable=num2)
num2_entered.grid(column=1,row=1)


#Adding a button
action = ttk.Button(win,text=" + ", command = add_me)
action.grid(column=2, row=1)
