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

