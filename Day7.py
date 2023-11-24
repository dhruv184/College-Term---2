'''
t1 = ()
t2 = (1,2,3,4,5,6,7,8)
print(t1)
print(t2[0])
print(t2[3:])
print(max(t2))
'''
#print("=======================")
'''
class User:
    
    def __init__(self, name , age ):
        self.name = name
        self.age = age

    def __str__(self):

        return f"Name : {self.name}  Age : {self.age}" 
    
t3 = (User("Tim" , 20) , User("Jane" , 25) , User("Mark" , 33))

print(id(0))

for user in t3:
    print(user)

t3[0].name = "Susan"

print(len(t3))

for user in t3:
    print(user)
'''
#print("=======================")
'''
def getUserInfo():

    name = input("Enter user name")
    age = input("Enter user age")

    return (name , age)

name , age = getUserInfo()
print(name)
print(age)
'''
#print("=======================")
