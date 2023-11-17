'''
from tkinter import *

root = Tk()
root.title("Pack Manager Example")
root.geometry("500x500")

label1 = Label(root, text = "Red" , bg = "red")
label1.pack(side = LEFT)

label2 = Label(root , text = "Green" , bg = "green")
label2.pack(side = LEFT)

label3 = Label(root , text = "Blue" , bg = "blue")
label3.pack(side = LEFT , fill = BOTH)

root.mainloop()
'''
#print("=======================")
'''
"""
The app should allow the user to enter
two numbers. when Submit
button is clicked add the numbers
and display the total. Using GUI.
"""
import tkinter as tk

root = tk.Tk()

root.title("GUI Example")
root.geometry("500x600")

for i in range(5):

    label1 = tk.Label(root , text = "Red" , background = "red")
    label1.pack(side = "left")

    label2 = tk.Label(root , text = "Green" , background = "green")
    label2.pack(side = "right")

    label3 = tk.Label(root , text = "Yellow" , background = "yellow")
    label3.pack(side = "top")

    label4 = tk.Label(root , text = "Blue" , background = "blue")
    label4.pack(side = "bottom")

root.mainloop()
'''
#print("=======================")
'''
import tkinter as tk

def action():

    name = entry.get()

    if len(name) > 0 :

        print("Hi" , name)
        resultLable1[ "text"] = f" Hi , {name}"

    else:

        print("Hi There")
        resultLable1[ "text"] = f" Hi There "

root = tk.Tk()
root.geometry("500x500")
root.title("GUI Interface")

lable1 = tk.Label(root , text = "User Name")
lable1.pack()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text = "Button 1" , command = action)
btn.pack()

resultLable1 = tk.Label(root , text = "Result : ")
resultLable1.pack()

root.mainloop()
'''
#print("=======================")
'''
"""Using Frame"""

import tkinter as tk

def action():

    name = entry.get()
    print(name)

root = tk.Tk()
root.geometry("500x500")

frame1 = tk.Frame(root , bg = "red")
frame1.pack(side = "top")

label1 = tk.Label(frame1, text = "User Name")
label1.pack(side = "top")

entry = tk.Entry(frame1)
entry.pack(side = "top")

btn = tk.Button(root , text = "Button 1" , command = action)
btn.pack()

root.mainloop()
'''
#print("=======================")
'''
"""Grid Example"""

import tkinter as tk

def getFullName():

    firstname = firstEntry.get()
    lastname = lastEntry.get()
    fullNameLabel[ "text"] = f" {firstname} {lastname}"

root = tk.Tk()
root.geometry("500x500")

firstLabel = tk.Label(root , text =  "First Name : ")
firstLabel.grid(row = 0 , column = 0)

lastLable = tk.Label(root , text =  "Last Name : ")
lastLable.grid(row = 1 , column = 0)

firstEntry = tk.Entry(root)
firstEntry.grid(row = 0 , column = 1)

lastEntry = tk.Entry(root)
lastEntry.grid(row = 1 , column = 1)

btn = tk.Button(root , text = "Submit" , command = getFullName)
btn.grid(row = 2 , column = 1)

fullNameLabel = tk.Label(root , text = " Full Name ")
fullNameLabel.grid(row = 3 , column = 1 , columnspan = 2)

root.mainloop()
'''
#print("=======================")
'''
"""Grid Example - 2 (Adding Frame)"""

import tkinter as tk

def getFullName():

    firstname = firstEntry.get()
    lastname = lastEntry.get()
    fullNameLabel[ "text"] = f" {firstname} {lastname}"

root = tk.Tk()
root.geometry("500x500")

frame1 = tk.Frame(root)
frame1.pack(side = "top")

firstLabel = tk.Label(frame1 , text =  "First Name : ")
firstLabel.grid(row = 0 , column = 0)

lastLable = tk.Label(frame1 , text =  "Last Name : ")
lastLable.grid(row = 1 , column = 0)

firstEntry = tk.Entry(frame1)
firstEntry.grid(row = 0 , column = 1)

lastEntry = tk.Entry(frame1)
lastEntry.grid(row = 1 , column = 1)

btn = tk.Button(frame1 , text = "Submit" , command = getFullName)
btn.grid(row = 2 , column = 1)

fullNameLabel = tk.Label(frame1 , text = " Full Name ")
fullNameLabel.grid(row = 3 , column = 1 , columnspan = 2)

root.mainloop()
'''
#print("=======================")
'''
"""Radio Button Example"""

import tkinter as tk

def action():

    if option.get() == 1:
        print("Option 1 is selected" , option.get())
    else:
        print("Option 2 is selected" , option.get())    
    

root = tk.Tk()
root.geometry("500x500")

option = tk.IntVar()
rbtn1 = tk.Radiobutton(root , text = "Option 1" , variable = option , value = 1)
rbtn1.pack()

rbtn2 = tk.Radiobutton(root , text = "Option 2" , variable = option , value = 2)
rbtn2.pack()

btn = tk.Button(root , text = "Submit" , command = action)
btn.pack()

root.mainloop()
'''
#print("=======================")
'''
"""
The app should allow the user to enter
two numbers. when Submit
button is clicked add the numbers
and display the total
"""

import tkinter as tk

def Sum():

    try:

        n1 = firstEntry.get()
        n2 = secondEntry.get()
        
        total = int(n1) + int(n2)

        SumLabel[ "text"] = f" Total = {total}"
        SumLabel["fg"] = "Black"

    except Exception as e:

        SumLabel["text"] = "Enter valid Numbers"
        SumLabel["fg"] = "red"

root = tk.Tk()
root.geometry("500x500")

frame1 = tk.Frame(root)
frame1.pack()

number1 = tk.Label(frame1 , text =  "Enter Number : ")
number1.grid(row =0 , column = 0)

number2 = tk.Label(frame1 , text =  "Enter Number : ")
number2.grid(row =1 , column = 0)

firstEntry = tk.Entry(frame1)
firstEntry.grid(row = 0 , column = 1)

secondEntry = tk.Entry(frame1)
secondEntry.grid(row = 1 , column = 1)

btn = tk.Button(frame1 , text = "Submit" , command = Sum)
btn.grid(row = 2 , column = 1)

SumLabel = tk.Label(frame1 , text = " Total = ")
SumLabel.grid(row = 3 , column = 1 , columnspan = 2)

root.mainloop()
'''
#print("=======================")
'''
"""
Develop GUI based Application: The app should allow the user to enter two numbers. 
when Submit button is clicked add / multiply the numbers and display the total
"""
import tkinter as tk

def Sum():

    try:
        if option.get() == 1:
            n1 = firstEntry.get()
            n2 = secondEntry.get()
            
            total = int(n1) + int(n2)

            SumLabel[ "text"] = f" Total = {total}"
            SumLabel["fg"] = "Black"

        else:
            n1 = firstEntry.get()
            n2 = secondEntry.get()
            
            Product = int(n1) * int(n2)

            SumLabel[ "text"] = f" Product = {Product}"
            SumLabel["fg"] = "Black"

    except Exception as e:

        SumLabel["text"] = "Enter valid Numbers"
        SumLabel["fg"] = "red"

root = tk.Tk()

frame1 = tk.Frame(root)
frame1.pack()

option = tk.IntVar()
rbtn1 = tk.Radiobutton(frame1 , text = "ADD" , variable = option , value = 1)
rbtn1.grid(row = 0 , column= 0 )

rbtn2 = tk.Radiobutton(frame1 , text = "Multiply" , variable = option , value = 2)
rbtn2.grid(row = 0 , column= 1 )

number1 = tk.Label(frame1 , text =  "Enter Number : ")
number1.grid(row =1 , column = 0)

number2 = tk.Label(frame1 , text =  "Enter Number : ")
number2.grid(row =2 , column = 0)

firstEntry = tk.Entry(frame1 , width= 10)
firstEntry.grid(row = 1 , column = 1)

secondEntry = tk.Entry(frame1 , width= 10)
secondEntry.grid(row = 2 , column = 1)

btn = tk.Button(frame1 , text = "Submit" , command = Sum)
btn.grid(row = 3 , column = 0 , columnspan = 2)

SumLabel = tk.Label(frame1 , text = " Total = ")
SumLabel.grid(row = 4 , column = 0 , columnspan = 2)

root.mainloop()
'''
#print("=======================")