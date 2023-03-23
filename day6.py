# file = open("practice6.txt", 'r')
#if file in line by line
# a=file.readlines()
# b=[]
# for i in a:
#     if int(i.strip())%2==0:
#         b.append(i.strip())
# print(b)
# file.close()
# a= file.read().strip() # for convert into \n from lines
# a=a.split("\n") # make a list with using \n


# if file contrnt in line
# a= file.read().split(",")
# print(a)

with open("practice6.txt", 'r') as file:
    a=file.readlines()
# even_file = open("evens.txt", 'a')
for i in a:
    if int(i.strip())%2==0:
        with open("evens.txt", 'a') as new_file:
            new_file.write(i)
            new_file.write("\n")

# with open("evens.txt", 'r') as new_file:
    
