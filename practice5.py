def sub(x, y):
    return x-y
def add(x, y):
    return x+y
x=int(input("Enter 1st value"))
y=int(input("Enter 2nd value"))
z=input("Type + for additon/ - for substraction")
if z=="+":
    print(add(x, y))
else:
    print(sub(x, y))

"""
we can also write functions as

def add(x, y):
    answer=x+y
    return answer
"""