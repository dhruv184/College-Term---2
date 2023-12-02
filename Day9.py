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