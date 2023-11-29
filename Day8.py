'''
import csv
with open ('user.csv','r') as file:

    reader = csv.reader(file)
    for row in reader:
        print(row)
'''
#print("=======================")
'''
"""
Exercise: Analyze CSV data

Create a CSV file named sales_data.csv with the following content:
Product,Quantity,Price
Laptop,10,800
Smartphone,30,400
Headphones,50,50
Monitor,15,

❑ Read the sales_data.csv file use the csv.reader() from the csv module
❑ Process the data and calculate the total revenue for each product (Quantity * Price).
❑ Print the results
"""
import csv

with open ('sales_data.csv' , 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    print("\nProduct & Revenue\n")
    for row in reader:
        revenue = float(row[1]) * float(row[2])
        print(f'{row[0]} : ${round(revenue,2)}')
'''
#print("=======================")
'''
"""
Exercise: Analyze CSV data and using CLASS 
 
Create a CSV file named sales_data.csv with the following content:
Product,Quantity,Price
Laptop,10,800
Smartphone,30,400
Headphones,50,50
Monitor,15,

❑ Read the sales_data.csv file use the csv.reader() from the csv module
❑ Process the data and calculate the total revenue for each product (Quantity * Price).
❑ Print the results
"""
class Product:

    def __init__(self , name , Qty , price):

        self.name = name
        self.quantity = Qty
        self.price = price
    
    def revenue(self):

        return self.quantity * self.price
    
    def __str__(self):

        return f'{self.name} : {self.revenue()}'

import csv

products = [ ]

with open('sales_data.csv' , 'r') as file:

    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        p = Product(row[0] , int(row[1]) , int(row[2]))
        products.append(p)

for p in products:
    print(p)        
'''

