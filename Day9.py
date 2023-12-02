'''
import json

with open("JsonFile.json" , "r") as file:

    data = json.load(file)
    print(data)
    print(type(data))
'''
#print("=======================")     
'''
import json

d = {"name" : "Tim" , "age" : 33}

with open('json_file_output.json' , 'w') as file:

    json.dump(d,file)
'''    
#print("=======================")
'''
import json

with open('JsonFile.json' , 'r') as file:

     data = json.load(file)

     print("Name =", data['Name'] )
     print("Age =", data['Age'])
     print("Phone", data['Phone'][0])
     print(type(data))
'''
#print("=======================")
'''
import json 

with open('students.json','r') as jsonFile:
   
   data =  json.load(jsonFile)
   print(type(data))

   for user in data:
      
      print(user['name'], user['age'],user['courses'][2])
      print(user['address']['city'])
'''      
#print("=======================")
'''
import json

with open('json_response.json' , 'r') as jsonfile:

    data = json.load(jsonfile)

    for emp in data :

        print(emp['id'],emp['name'] , emp['company']['name'])
'''
#print("=======================")
'''
import json

d = [{"name" : "Tim" ,"age" : 33}]

name = input('Enter username: ')
age = input("enter user age: ")
user = {'name':name, 'age':age}

d.append(user)

with open('json_file_output.json' , 'w') as file:
    json.dump(d,file , indent=2)
''' 
#print("=======================")   