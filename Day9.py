import json

with open("JsonFile.json" , "r") as file:

    data = json.load(file)
    print(data)
    print(type(data))