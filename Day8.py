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
