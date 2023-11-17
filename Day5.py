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