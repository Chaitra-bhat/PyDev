import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
check3.grid(column=2,row=4) #sticky=tk.W)

#Radiobutton Global
COLOR1 = 'Alice Blue'
COLOR2 = 'Black'
COLOR3 = 'Red'

#Radiobutton click
def radCall():
    radSel = radVar.get()
    if radSel==1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)

#create three radiobutton using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(win,text=COLOR1,variable=radVar, value=1,command=radCall)
rad1.grid(column = 0, row=5, sticky=tk.W,columnspan=3)

rad2 = tk.Radiobutton(win,text=COLOR2,variable=radVar, value=2,command=radCall)
rad2.grid(column = 1, row=5, sticky=tk.W,columnspan=3)

rad3 = tk.Radiobutton(win,text=COLOR3,variable=radVar, value=3,command=radCall)
rad3.grid(column = 2, row=5, sticky=tk.W,columnspan=3)

#scrolled text control
scrol_w = 30    # gives width of the box 
scrol_h = 6     #gives height of the box
scr = scrolledtext.ScrolledText(win,width=scrol_w,height=scrol_h, wrap=tk.WORD)     #tk.Word makes the long words come on next line it wraps the complete word  
scr.grid(column=0,columnspan=3)

name_entered.focus()    #place cursor on the entry box

#Start GUI
win.mainloop()

          
