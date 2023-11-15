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
