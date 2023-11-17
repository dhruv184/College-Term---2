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
