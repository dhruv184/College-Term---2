import csv
with open ("user.csv",'r') as file:

    reader = csv.reader(file)
    for row in reader:
        print(row)




'''
import csv

def get_user_info():

    name = input("Enter Name : ")
    age = input("Enter Age : ")
    city = input("Enter City : ")

def write_to_csv(file_name , data):

    with open(file_name , "a" , newline=" ") as csvfile:

        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data)
'''
