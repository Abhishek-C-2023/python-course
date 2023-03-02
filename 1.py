L=[]
L2=[]
L3=[]
a=int(input("Limit"))
for i in range(a):
    y=int(input())
    L.append(y)
for i in L:
    if i%2==0:
        L2.append(i)
    else:
        L3.append(i)
print("Even numbers is",L2)
print("Odd numers is",L3)