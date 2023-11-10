
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