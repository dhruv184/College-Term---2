'''
"""
Makind File
"""
file = open("myFile.txt" , "w")
file.write("Welcome to Python")
file.close()
'''
#print("=======================")
'''
def WriteToFile():
    file = open("myFile.txt" , "w")
    file.write("List of Names\n")
    for i in range(3):
        name = input(f"{i+1} : Enter user Name : ")
        file.write(name+"\n")
    file.close()

def ReadData(fileName):

    file =  open(fileName , "r")
    data = file.read()
    print(data)

ReadData("myFile.txt")    
'''
#print("=======================")
