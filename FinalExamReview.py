'''
"""
Create python application that allow the
owner of a product store owner to perform
the following tasks:
1.Display the list of products
2.Add a new product
3.Search for a specific product
"""

import csv

class Product:

    def __init__(self , id , name ,price):

        self.id = id 
        self.name = name
        self.price = price

    def __str__(self):

        return f"\nId : {self.id} , Name : {self.name} , Price : {self.price}"

class Store:

    def __init__(self):

        self.products = Data.getData('dataProducts.csv')           

    def addProduct(self , product ):

        self.products.append(product)

    def getProducts(self):

        return self.products
    
    def findProduct(self, id):

        p = None

        for product in self.products:

            if product.id == id:

                p = product
                break
        
        return p
    
    def saveData(self):

        rows = [ ]

        for p in self.products:

            row = [p.id , p.name , p.price]
            rows.append(row)

        Data.writeData('dataProducts.csv' , rows)    

    def updateProduct(self,product):

        p = self.findProduct(product.id)

        if isinstance(p , Product):

            p.name = product.name
            p.price = product.price    

class Data :
    
    @staticmethod
    def getData( filename ):
        
        products = [ ]

        with open(filename , "r") as file:

            reader = csv.reader(file)

            for row in reader:

                p = Product(row[0] , row[1] , row[2])
                products.append(p)

        return products     
       
    @staticmethod
    def writeData(filename,rows):
        
        with open(filename ,'w' , newline='' ) as file:

            writer = csv.writer(file)

            writer.writerows(rows)

store = Store()

def displayMainMenu():

    print("\nPlease select One of the following Options : \n")

    print("1 to Add Products\n")
    print("2 to View the list of Products\n")
    print("3 to Find Products\n")
    print("4 to Save in File\n")
    print("5 to Update\n")
    print("6 to Delete\n")
    print("7 to Exit\n")

while True :     
    
    displayMainMenu()

    x = int(input(" :->: "))
    
    if x == 1 :
        
        print("\n")
        id = input("Enter Product id : ")
        name = input("Enter product Name : ")
        price = input("Enter product price : ")

        p = Product(id,name,price)

        store.addProduct(p)

    elif x == 2 :

        print("\nList of Products : \n")

        for p in store.getProducts():

            print(p)    

    elif x == 3 :
        
        print("\n")
        id = input("Enter Product id to Find Product : ")

        p = store.findProduct(id)

        if isinstance(p , Product):

            print(p)

        else:

            print(f"Product with ID = {id} [ Not Found ] ")   

    elif x == 4:

        store.saveData()

    elif x == 5:

        print("\n")
        id = input("Enter Product id to Update Product : ")    
        print("\n")
        newName = input("Enter Updated Name : ")
        newPrice = input("Enter Updated Price : ")

        p = Product(id , newName , newPrice)

        store.updateProduct(p)

    elif x == 7 :

        print("\n Thanks You \n")
        break   
'''    
#print("=======================")  

"""
Create python application that allow the
owner of a product store owner to perform
the following tasks:
1.Display the list of products
2.Add a new product
3.Search for a specific product
Using GUI Interface
"""
import csv

class Product:

    def __init__(self , id , name ,price):

        self.id = id 
        self.name = name
        self.price = price

    def __str__(self):

        return f"\nId : {self.id} , Name : {self.name} , Price : {self.price}"

class Store:

    def __init__(self):

        self.products = Data.getData('dataProducts.csv')           

    def addProduct(self , product ):

        self.products.append(product)

    def getProducts(self):

        return self.products
    
    def findProduct(self, id):

        p = None

        for product in self.products:

            if product.id == id:

                p = product
                break
        
        return p
    
    def saveData(self):

        rows = [ ]

        for p in self.products:

            row = [p.id , p.name , p.price]
            rows.append(row)

        Data.writeData('dataProducts.csv' , rows)    

    def updateProduct(self,product):

        p = self.findProduct(product.id)

        if isinstance(p , Product):

            p.name = product.name
            p.price = product.price    

class Data :
    
    @staticmethod
    def getData( filename ):
        
        products = [ ]

        with open(filename , "r") as file:

            reader = csv.reader(file)

            for row in reader:

                p = Product(row[0] , row[1] , row[2])
                products.append(p)

        return products     
       
    @staticmethod
    def writeData(filename,rows):
        
        with open(filename ,'w' , newline='' ) as file:

            writer = csv.writer(file)

            writer.writerows(rows)

store = Store()

import tkinter as tk
from tkinter import messagebox , simpledialog

class MainMenuGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.store = Store()

        self.title("Product Management System")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Please select one of the following options:")
        label.pack(pady=10)

        buttons = [
            ("Exit", self.exit_program),
            ("View Products", self.view_products),
            ("Add Product", self.add_product),
            ("Find Product", self.find_product),
            ("Save Data", self.save_data),
            ("Update Product", self.update_product),
        ]

        for text, command in buttons:
            button = tk.Button(self, text=text, command=command)
            button.pack(pady=5)

    def display_products(self, products):
        result = ""
        for p in products:
            result += str(p) + "\n"
        messagebox.showinfo("List of Products", result)

    def exit_program(self):
        self.destroy()

    def view_products(self):
        products = self.store.getProducts()
        self.display_products(products)

    def add_product(self):
        id = simpledialog.askstring("Input", "Enter product id:")
        name = simpledialog.askstring("Input", "Enter product name:")
        price = simpledialog.askstring("Input", "Enter product price:")
        p = Product(id, name, price)
        self.store.addProduct(p)

    def find_product(self):
        id = simpledialog.askstring("Input", "Enter product id:")
        p = self.store.findProduct(id)
        if isinstance(p, Product):
            self.display_products([p])
        else:
            messagebox.showinfo("Product Not Found", f"Product with id = {id} is not found")

    def save_data(self):
        self.store.saveData()
        messagebox.showinfo("Save Data", "Data saved successfully")

    def update_product(self):
        id = simpledialog.askstring("Input", "Enter product id:")
        new_name = simpledialog.askstring("Input", "Enter new name:")
        new_price = simpledialog.askstring("Input", "Enter new price:")
        p = Product(id, new_name, new_price)
        self.store.updateProduct(p)
        messagebox.showinfo("Update Product", "Product updated successfully")

if __name__ == "__main__":
    app = MainMenuGUI()
    app.mainloop()
