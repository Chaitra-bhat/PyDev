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
    curRad = tk.Radiobutton(win,text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col,row=5,sticky=tk.W)


#scrolled text control
scrol_w = 30    # gives width of the box 
scrol_h = 6     #gives height of the box
scr = scrolledtext.ScrolledText(win,width=scrol_w,height=scrol_h, wrap=tk.WORD)     #tk.Word makes the long words come on next line it wraps the complete word  
scr.grid(column=0,columnspan=3)


#Create a container to hold labels
buttons_frame = ttk.LabelFrame(win,text='Labels in a frame')
buttons_frame.grid(column=0,row=7, padx=20, pady=40)

#place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0,row=0,sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0,row=1,sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0,row=2,sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8,pady=4)

    
name_entered.focus()    #place cursor on the entry box

#Start GUI
win.mainloop()

          
