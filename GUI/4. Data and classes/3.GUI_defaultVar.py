import tkinter as tk

#Create instance
win  =  tk.Tk()

#assign tkinter variable to strdata variable
strData = tk.StringVar()

#set strData variable
strData.set('Hello StringVar')

#get value of string var
varData = strData.get()

#print the data
print(varData)

#print out the default tkinter variabl values
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())
print(tk.StringVar())
