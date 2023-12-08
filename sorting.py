'''
l1 = [1,2,4,7,-3,-2]
l1.sort()
print(l1)

l3 = sorted(l1, reverse = True)
print(l3)
'''
#print("=======================")
'''
l1 = [1,2,4,7,-3,-2]
l1.sort()
print(l1)
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
l3 = sorted(l1, reverse = True , key = absolute)
print(l3)
'''
#print("=======================")
'''
"""
You will be sorting the following list by each element’s 
second letter, a to z.Create a function to use when sorting, 
called second_let. It will take a string as input and return 
the second letter of that string. Then sort the list, create
a variable called sorted_by_second_let and assign the sorted 
list to it.Do not use lambda.
"""
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(e):

    return e[1]

sorted_by_second_let = sorted(ex_lst , key = second_let)
print(sorted_by_second_let)
'''
#print("=======================")