'''
"""
Exception Handling Example
"""

while True:
    try:
        
        x = int(input("Enter a number : "))
        result = 10/x
        print(result)
        break

    except ValueError as e:

        print("Error" , e)

    except ZeroDivisionError as ex:

        print("Error 2" , ex)    

    except Exception as e:

        print("ERROR" , e)

print("done")
'''
#print("=======================") 

def divide( a , b ):

    try:
        result = a/b

    except :

        return ' Division by zero id not allowed '

    else:

        return result

r = divide( 2 , 3 ) 
print("Result = ", r )       