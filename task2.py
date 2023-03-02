L=[]
L2=[]
x=int(input("Enter the limit of numbers"))
for i in range(x):
    y=int(input())
    L.append(y)
for i in L:
    if i%2==0:
        L2.append(i)
print(L2)
