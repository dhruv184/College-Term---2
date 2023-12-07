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
'''
"""
Create python application that allow the
owner of a product store owner to perform
the following tasks:
1.Display the list of products
2.Add a new product
3.Search for a specific product
Using GUI Interface
"""
import tkinter as tk
import csv

class Product:

    def __init__(self , id , name ,price):

        self.id = id 
        self.name = name
        self.price = price

    def __str__(self):

        return f"Id : {self.id}\nName : {self.name}\nPrice : {self.price}\n"

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

class ProductStoreGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Store Management System")
        
        self.store = Store()

        # Create labels and entry widgets
        self.label_id = tk.Label(master, text="Product ID:")
        self.entry_id = tk.Entry(master)

        self.label_name = tk.Label(master, text="Product Name:")
        self.entry_name = tk.Entry(master)

        self.label_price = tk.Label(master, text="Price:")
        self.entry_price = tk.Entry(master)

        # Create display box
        self.display_box = tk.Text(master, height=10, width=40)
        self.display_box.grid(row=0, column=2, rowspan=9, padx=10, pady=5)

        # Create buttons
        self.button_view = tk.Button(master, text="View Productss", command=self.view_products)
        self.button_add = tk.Button(master, text="Add Products", command=self.add_product)
        self.button_find = tk.Button(master, text="Find Products", command=self.find_product)
        self.button_save = tk.Button(master, text="Save Products", command=self.save_data)
        self.button_update = tk.Button(master, text="Update Product", command=self.update_product)
        self.button_exit = tk.Button(master, text="Exit", command=self.master.destroy)

        # Arrange widgets using grid
        self.label_id.grid(row=0, column=0, padx=10, pady=5)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        self.label_name.grid(row=1, column=0, padx=10, pady=5)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        self.label_price.grid(row=2, column=0, padx=10, pady=5)
        self.entry_price.grid(row=2, column=1, padx=10, pady=5)

        self.button_view.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_find.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_save.grid(row=6, column=0, columnspan=2, pady=10)
        self.button_update.grid(row=7, column=0, columnspan=2, pady=10)
        self.button_exit.grid(row=8, column=0, columnspan=2, pady=10)

    def view_products(self):
        self.clear_entries()
        self.display_box.delete(1.0, tk.END)  # Clear the display box
        self.display_box.insert(tk.END, "List of products:\n")
        for p in self.store.getProducts():
            self.display_box.insert(tk.END, str(p) + "\n")

    def add_product(self):
        product_id = self.entry_id.get()
        product_name = self.entry_name.get()
        product_price = self.entry_price.get()
        product = Product(product_id, product_name, product_price)
        self.store.addProduct(product)
        self.clear_entries()

    def find_product(self):
        product_id = self.entry_id.get()
        product = self.store.findProduct(product_id)
        self.display_box.delete(1.0, tk.END)  # Clear the display box
        if isinstance(product, Product):
            self.display_box.insert(tk.END, str(product))
        else:
            self.display_box.insert(tk.END, f"Book with id = {product_id} is not found")
        self.clear_entries()

    def save_data(self):
        self.store.saveData()
        self.display_box.delete(1.0, tk.END)  # Clear the display box
        self.display_box.insert(tk.END, "Data saved successfully")

    def update_product(self):
        product_id = self.entry_id.get()
        new_name = self.entry_name.get()
        new_price = self.entry_price.get()
        product = Product(product_id, new_name, new_price)
        self.store.updateProduct(product)
        self.clear_entries()

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)

root = tk.Tk()
app = ProductStoreGUI(root)
root.mainloop()
'''
#print("=======================")  