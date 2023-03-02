a=input("Enter a name")
x=False
for i in a:
    if i.isupper():
        print(i)
        x=True
if not x:
    print("No upper case")
