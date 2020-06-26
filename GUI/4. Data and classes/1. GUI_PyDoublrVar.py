import tkinter as tk

#create an instance of tkinter
win = tk.Tk()

#Create a double Var
doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.4)
print(type(doubleData))

add_double =  1.2222 + doubleData.get()
print(add_double)
print(type(add_double))
