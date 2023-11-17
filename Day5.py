'''
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

textWidget = tk.Text(root, height= 6)
textWidget.pack()

textWidget.insert(tk.END, "Hello \nthis is a \ntext widget")

txt = textWidget.get("1.0" , "end")
print(txt)
root.mainloop()
'''
#print("=======================")
'''
import tkinter as tk

from tkinter import ttk

def action():

    if option1.get() == "1":
        print("option is selected")

    elif size.get() == 1:
        print("Size = Small")    
    
    elif size.get() == 2:
        print("Size = Medium")

    elif size.get() == 3:
        print("Size = Large") 

    else:
        print("option 1 is not selected")    
        

root = tk.Tk()
root.geometry("300x300")

option1 = tk.StringVar()

cb1 = ttk.Checkbutton(root, text = "Option 1" , variable = option1 , onvalue = 1 , offvalue = 0) 
cb1.pack()

label1 = ttk.Label(root, text = "Select Pizza Size")
label1.pack()

frame1 = tk.Frame(root)
frame1.pack()

size = tk.IntVar()

rbtn1 = ttk.Radiobutton(frame1 , text = "Small " , variable = size , value = 1)
rbtn1.pack(side = "left")

rbtn2 = ttk.Radiobutton(frame1 , text = "Medium " , variable = size , value = 2)
rbtn2.pack(side = "left")

rbtn3 = ttk.Radiobutton(frame1 , text = "Large " , variable = size , value = 3)
rbtn3.pack(side = "left")

btn1 = ttk.Button(root , text = "Button 1" , command = action)
btn1.pack()

root.mainloop()
'''
#print("=======================")
'''
import tkinter as tk

from tkinter import ttk

def action():

    option = comboBox.get()
    print(option)
    
    s = listBox.curselection()
    index = s[0]

    print(s , mylist[index])
    
root = tk.Tk()
root.geometry("500x500")

label1 = ttk.Label(root , text = "Select Pizza Size")
label1.pack()

comboBox = ttk.Combobox(root , values = ["Small" , "Medium" , "Large"])
comboBox.pack()

btn = ttk.Button(root , text = "Select" , command = action)
btn.pack()

mylist = ["Python" , "Java" , "C#" , "C++"]

var = tk.StringVar(value = mylist)

listBox = tk.Listbox(root , listvariable = var , selectmode = "extended")
listBox.pack()

root.mainloop()
'''
#print("=======================")
'''
import tkinter as tk
from tkinter import ttk

def action():
    value = slider.get()
    print("Value = ",round(value))

root = tk.Tk()
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(fill = "both" , expand = True)

frame1 = tk.Frame(notebook , bg = "red")
frame1.pack(fill = "both" , expand = True)

frame2 = tk.Frame(notebook , bg = "green")
frame2.pack(fill = "both" , expand = True)

notebook.add(frame1 , text = "Page 1")
notebook.add(frame2 , text = "Page 2")

label = ttk.Label(frame1 , text = "Select Pizza Size")
label.pack()

comboBox = ttk.Combobox(frame1 , values = ["Small" , "Medium" , "Large"])
comboBox.pack()

slider = ttk.Scale(frame2 , from_= 0 , to = 1000 , orient =tk.HORIZONTAL) 
slider.pack()

btn = ttk.Button(frame2 , text = "Get Data" , command = action)
btn.pack()

root.mainloop()
'''
#print("=======================")
'''
import tkinter as tk

from tkinter import ttk

from tkinter import filedialog

def action():
    value = slider.get()
    print("Value = ",round(value))
    
    textWidget.delete("1.0" , "end")
    
    filename = filedialog.askopenfilename()

    file = open(filename , "r")
    txt = file.read()
    textWidget.insert(tk.END, txt)
    file.close()

root = tk.Tk()
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack(fill = "both" , expand = True)

frame1 = tk.Frame(notebook , bg = "red")
frame1.pack(fill = "both" , expand = True)

frame2 = tk.Frame(notebook , bg = "green")
frame2.pack(fill = "both" , expand = True)

notebook.add(frame1 , text = "Page 1")
notebook.add(frame2 , text = "Page 2")

label = ttk.Label(frame1 , text = "Select Pizza Size")
label.pack()

comboBox = ttk.Combobox(frame1 , values = ["Small" , "Medium" , "Large"])
comboBox.pack()

slider = ttk.Scale(frame2 , from_= 0 , to = 1000 , orient =tk.HORIZONTAL) 
slider.pack()

btn = ttk.Button(frame2 , text = "Get Data" , command = action)
btn.pack()

textWidget = tk.Text(frame2)
textWidget.pack()

root.mainloop()
'''
#print("=======================")

import tkinter as tk

from tkinter import ttk 

from tkinter import filedialog

def action():

    filename = filedialog.askopenfilename()

    file = open("ProductFile.txt" , "w")
    file.write(filename)
    file.close()
    
    file = open("ProductFile.txt", "r")
    txt = file.read()
    textWidget.insert(tk.END, txt)
    file.close()


root = tk.Tk()
root.title("Product infomation")
root.geometry("400x400")

label1 = ttk.Label(root , text = "Product infomation")
label1.pack()

frame1 = tk.Frame(root)
frame1.pack()

label2 = ttk.Label(frame1 , text = "Name")
label2.grid(row = 0 , column = 0)

entry = tk.Entry(frame1)
entry.grid(row = 0 , column = 1)

label3 = ttk.Label(frame1 , text = "Product")
label3.grid(row = 1 , column = 0)

entry = tk.Entry(frame1)
entry.grid(row = 1 , column = 1)

btn1 = ttk.Button(frame1 , text = "Save To File" , command = action)
btn1.grid(row = 2 , column = 1 , columnspan = 2)

btn2 = ttk.Button(frame1 , text = "Read From File" , command = action)
btn2.grid(row = 3 , column = 1 , columnspan = 2)

textWidget = tk.Text(frame1)
textWidget.grid(row = 4 , column = 1 , columnspan = 2)

root.mainloop()