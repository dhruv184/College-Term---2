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
#print("=======================")
'''
import csv

data = []

row1 = ["Porduct" , "Quantity" , "Price"]
row2 = ["Laptop" , 10 , 800]
row3 = ["Smartphone" , 30 , 400]

data.append(row1)
data.append(row2)
data.append(row3)

name = input("Enter Product Name : ")
qty = input("Enter quantity : ")
price = input("Enter Price : ")

row4 = [name , qty , price]
data.append(row4)

with open('sales_data_output.csv' , 'w' , newline = '') as file:

    writer = csv.writer(file)
    writer.writerows(data)
'''
#print("=======================")
'''
"""
Exercise: Managing User Data with CSV

Create a Python program that asks users to input information (e.g. name, age, and city) for
multiple users.

❑ Write this user data to a CSV file named user_data.csv.
❑ Read the contents of user_data.csv and display the information.
❑ Instructions:
▪ Use the get_user_info() function to collect information for each user.
▪ Use the csv.writer to write the list of user data to the CSV file.
▪ Use the csv.reader to read and display the contents of the CSV file.
▪ Feel free to modify the exercise based on your preferences or add more tasks if needed
"""

import csv

def get_user_info():

    name = input("Enter Name : ")
    age = input("Enter Age : ")
    city = input("Enter City : ")

    return [name , age , city]

def wirte_to_csv(file_name , data):

    with open(file_name , 'a' , newline = '') as file:

        writer = csv.writer(file)
        writer.writerows(data)

def read_and_display_csv(file_name):

    with open(file_name , 'r') as file:

        reader = csv.reader(file)
        for row in csv.reader(file):
            print(row)

user_data_file = "user_data.csv"

user_info = get_user_info()

print(user_info)

print(wirte_to_csv(user_data_file, user_info))

print(read_and_display_csv(user_data_file))
'''
#print("=======================")
'''
"""
Second Method:

Exercise: Managing User Data with CSV

Create a Python program that asks users to input information (e.g. name, age, and city) for
multiple users.

❑ Write this user data to a CSV file named user_data.csv.
❑ Read the contents of user_data.csv and display the information.
❑ Instructions:
▪ Use the get_user_info() function to collect information for each user.
▪ Use the csv.writer to write the list of user data to the CSV file.
▪ Use the csv.reader to read and display the contents of the CSV file.
▪ Feel free to modify the exercise based on your preferences or add more tasks if needed
"""

import csv

def get_user_info():

    name = input("Enter Name : ")
    age = input("Enter Age : ")
    city = input("Enter City : ")

    return (name , age , city)

users  = [ ]

while True:

    answer = input("Would you like to add a user (yes / no) : ")

    if answer == "yes":

        user = get_user_info()
        users.append(user)

    else:

        print("Thank You")
        break

headers = ["Name" , "Age" , "City"]

with open ("user_data_2.csv" , "w" , newline = '') as csvFile:

    writer = csv.writer(csvFile)
    writer.writerow(headers)
    writer.writerows(users)

with open("user_data_2.csv" , 'r') as file:
        
        reader = csv.reader(file)
        for row in csv.reader(file):
            print(row)
        
        reader = csv.DictReader(file)
        for row in reader:
             print(row)    
'''
#print("=======================")             
'''
"""
Input csv file:-

Name weeklyHours HourlyRate
Tim     30         20
Jane    25         25
Joe     35         21

Output csv file:-

Name    wages
Tim      600
Jane     525
Joe      735
 
"""

import csv

data = []

row1 = ["Name" , "Weekly Hours" , "Hourly Rate"]
row2 = ["Tim" , 30 , 20]
row3 = ["Jane" , 25 , 25]
row4 = ["Joe" , 35 , 21]

data.append(row1)
data.append(row2)
data.append(row3)
data.append(row4)

with open('Working_Data.csv' , 'w' , newline = '') as file:

    writer = csv.writer(file)
    writer.writerows(data)

with open ('Working_Data.csv' , 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        revenue = float(row[1]) * float(row[2])
        print(f'{row[0]} : ${round(revenue,2)}')    
'''        
#print("=======================")     
'''
import csv

output = []
with open ('Working_Data.csv' , 'r') as file:
    reader = csv.DictReader(file)
    print("Name \t Weges")

    for row in reader:
        wage = int(row['Hours']) * int (row["Rate"])
        print(f'{row["Name"]} \t {wage}')

        d = [ "Name":row["Name"] , "Weges":wage]
        output.append(d)

with open('Working_Data_Out.csv' , 'w' , newline = '') as file:

    writer = csv.writer(file)
    writer.writerows(output)         
                
'''