
"""
Create python application that allow the
owner of a product store owner to perform
the following tasks:
1.Display the list of products
2.Add a new product
3.Search for a specific product
"""

class Product:

    def __init__(self , id , name ,price):

        self.id = id 
        self.name = name
        self.price = price

    def __str__(self):

        return f"Id : {self.id} , Name : {self.name} , Price : {self.price}"

class Store:

    def __init__(self):

        self.products = []           

    def addProduct(self , product ):

        self.products.append(product)

    def getProducts(self):

        return self.products

store = Store()

def displayMainMenu():

    print("\nPlease select One of the following Options : \n")

    print("1 to View the list of Products\n")
    print("2 to Add Products\n")
    print("3 to Find Products\n")
    print("4 to Exit\n")

while True :     
    
    x = int(input(" ::-> \n"))

    displayMainMenu()
    
    if x == 1 :

        print("\nList of Products : \n")

        for p in store.getProducts():

            print(p)
    
       