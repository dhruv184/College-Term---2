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