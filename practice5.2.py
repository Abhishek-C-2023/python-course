# x=10
# def vara(x):
#     x=20
#     return x
# x= vara(x)
# print(x)

# def a():
#     print("a")
#     def b():
#         print("b")
#     b()
# a()

def calculator():
    def sub(x, y):
        return x-y
    def add(x, y):
        return x+y
    x=int(input("Enter 1st value"))
    y=int(input("Enter 2nd value"))
    z=input("Type + for additon/ - for substraction")
    if z=="+":
        # print(add(x, y))
        a=add(x, y)
    else:
        # print(sub(x, y))
        a=sub(x, y)
    return a
print(calculator()*10)

