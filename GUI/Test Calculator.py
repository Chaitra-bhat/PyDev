import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#Add a title
win.title("Chaitra's calculator")

# adding python icon
win.iconbitmap('calc.ico')

#Adding label for number 1
a_label = ttk.Label(win,text="First number: ")
a_label.grid(column=0,row=0)

#Adding label for number 2
b_label = ttk.Label(win,text="Second number: ")
b_label.grid(column=2,row=0)

#Adding a Text Box Entry widget for first Number
num1 = tk.IntVar()
num1_entered = ttk.Entry(win,width=12,textvariable=num1)
num1_entered.grid(column=0,row=1, padx = 12, pady = 12)

#Adding a Text Box Entry widget for second Number
num2 = tk.IntVar()
num2_entered = ttk.Entry(win,width=12,textvariable=num2)
num2_entered.grid(column=2,row=1, padx = 12, pady = 12)

#adding text box for answer
ans_got = tk.DoubleVar()
answer = ttk.Entry(win, width = 15, textvariable = ans_got)
answer.grid(column = 1, row = 2, padx = 12, pady = 12)

#ERROR message
def msg_error():
    msg.showerror('Error message', 'This code has a error')
    
#function calls for addition
def addition():
    add_ans = num1.get() + num2.get()
    ans_got.set(add_ans)

#function calls for subtraction
def subtraction():
    sub_ans = num1.get() - num2.get()
    ans_got.set(sub_ans)

#function calls for multiplication
def multiplication():
    mul_ans = num1.get() * num2.get()
    ans_got.set(mul_ans)

#function calls for multiplication
def division():
    div_ans = num1.get() / num2.get()
    ans_got.set(div_ans)    
    
#adding buttons for addition
add_op = ttk.Button(win, text = '+', command = addition) #,  height = 8, width =  4)
add_op.grid(column = 0, row = 3, pady = 10)

#adding button for subtraction
sub_op = ttk.Button(win, text = '-', command = subtraction) #,  height = 8, width =  4)
sub_op.grid(column = 1, row = 3, pady = 10)

#adding button for multiplication
mul_op = ttk.Button(win, text = 'x', command = multiplication) #,  height = 8, width =  4)
mul_op.grid(column = 2, row = 3, pady = 10)

#adding button for multiplication
div_op = ttk.Button(win, text = '/', command = division) #,  height = 8, width =  4)
div_op.grid(column = 0, row = 4, pady = 10)





