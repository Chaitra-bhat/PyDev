import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from datetime import date
from datetime import time
from datetime import datetime

#create instance
win = tk.Tk()

#Add a title
win.title("Python GUI")

#creating tabs
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text="Tab 1")

#creating another tab
tab2 = ttk.Frame(tabControl)  #create a tab
tabControl.add(tab2,text="Tab 2") #add the tab


#creating a container frame to hold all other widgets
mighty = ttk.LabelFrame(tab1,text='Mighty Python')
mighty.grid(column=0,row=0,padx=8,pady=4)

#Creating another mighty tab to update in tab2 
mighty2 = ttk.LabelFrame(tab2,text='Mighty 2 python')
mighty2.grid(column = 1, row=0, padx=8, pady=4)


#Adding label for tab 2
a_label = ttk.Label(mighty2,text="Enter your age: ")
a_label.grid(column=0,row=0)

#Button click
def click_me():
    action.configure(text = 'Hello ' + name1.get()+ ' '  + number.get())

#Changing label
a_label = ttk.Label(mighty,text="Enter your name: ")
a_label.grid(column=0,row=0)

#Adding a Text Box Entry widget
name1 = tk.StringVar()
name_entered = ttk.Entry(mighty,width=12,textvariable=name1)
name_entered.grid(column=0,row=1)

#Adding a button
action = ttk.Button(mighty,text="Click Me!", command = click_me)
action.grid(column=2, row=1)

ttk.Label(mighty,text='Choose a number:').grid(column=1,row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty,width=12,textvariable=number,state='readonly')
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text='Disabled', variable=chVarDis,state='disabled')
check1.deselect()
check1.grid(column=0,row=4)#sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4)#sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2,row=4) #sticky=tk.W)

#Radiobutton Global make it list
colors = ['Alice Blue','Gold','Red']

# Change the callback function to be zero based using the list instead
# of module - level globl variabls
#Radiobutton click
def radCall():
    radSel = radVar.get()
    if radSel==0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

#create three radiobutton using one variable
radVar = tk.IntVar()

#We are selecting a non-existing index value for radvar
radVar.set(99)

# Now creating all three radiobuttons widgets within one loop
for col in range(3):
    curRad = tk.Radiobutton(mighty2,text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col,row=5,sticky=tk.W)


#scrolled text control
scrol_w = 30    # gives width of the box 
scrol_h = 6     #gives height of the box
scr = scrolledtext.ScrolledText(mighty,width=scrol_w,height=scrol_h, wrap=tk.WORD)     #tk.Word makes the long words come on next line it wraps the complete word  
scr.grid(column=0,columnspan=3)


#Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty,text='Labels in a frame')
buttons_frame.grid(column=0,row=7, padx=20, pady=40)

#place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0,row=1,sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0,row=2,sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8,pady=4)

#Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# creating a menubar
menu_bar = Menu(win)
win.config(menu=menu_bar)

#creating menu and add menu items
file_menu = Menu(menu_bar, tearoff=0) # tearoff removes a dotted line exsiting before
file_menu.add_command(label = "New File")
file_menu.add_separator()
file_menu.add_command(label = "Open")
#file_menu.add_separator()
file_menu.add_command(label = "Open Module")
#file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File",menu=file_menu)


todays_date = date.today()

#Display a message box
def _msgBox():
    msg.showinfo('Python Message Info Box', ' A python GUI created using tkinter:\nToday is ' + str(todays_date))
    
#adding another help option
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command = _msgBox )
menu_bar.add_cascade(label="Help", menu = help_menu)

#Warning message for run module
def _msgwarning():
    msg.showwarning('Warning message', 'Are you sure you want to run the module ?\n ')
    

#adding another run menu bar
run_menu = Menu(menu_bar, tearoff=0)
run_menu.add_command(label="Run Module", command = _msgwarning)
run_menu.add_separator()
run_menu.add_command(label="Check Module")
#run_menu.add_separator()
run_menu.add_command(label="Python shell")
menu_bar.add_cascade(label="Run", menu=run_menu)

tabControl.pack(expand=1,fill="both")   #pack to make visible

name_entered.focus()    #place cursor on the entry box

#Start GUI
win.mainloop()

          
