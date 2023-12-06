
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

        return f"\nId : {self.id} , Name : {self.name} , Price : {self.price}"

class Store:

    def __init__(self):

        self.products = []           

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

store = Store()

def displayMainMenu():

    print("\nPlease select One of the following Options : \n")

    print("1 to Add Products\n")
    print("2 to View the list of Products\n")
    print("3 to Find Products\n")
    print("4 to Exit\n")

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

    elif x == 4 :

        print("\n Thanks You \n")
        break        