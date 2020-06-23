import tkinter as tk
from tkinter import ttk

#create instance
win = tk.Tk()

#Add a title
win.title("Python GUI")

#Button click
def click_me():
    action.configure(text = 'Hello ' + name1.get()+ ' '  + number.get())

#Changing label
ttk.Label(win,text="Enter your name: ").grid(column=0,row=0)

#Adding a Text Box Entry widget
name1 = tk.StringVar()
name_entered = ttk.Entry(win,width=12,textvariable=name1)
name_entered.grid(column=0,row=1)

#Adding a button
action = ttk.Button(win,text="Click Me!", command = click_me)
action.grid(column=2, row=1)

#Creating three checkbutton
ttk.Label(win,text='Choose a number:').grid(column=1,row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis,state='disabled')
check1.deselect()
check1.grid(column=0,row=4)#sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4)#sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2,row=4)#sticky=tk.W)

name_entered.focus()    #place cursor on the entry box

#Start GUI
win.mainloop()

          
