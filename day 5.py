# To take input from user and store in dict
a=input("Enter a name").lower().replace(" ","") #line 2 or this b=a.lower() replace("parameter","change to parameter")
d={}
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
# To find out most_occurring_letter
most_occurring = 0
most_occurring_letter = str() #or we can use ""
for i in d: #we can use any variable name for i
    if d[i] >= most_occurring:    #2 1 2 > value print 1st occuring >= print last occuring
        most_occurring = d[i]
        most_occurring_letter = i

print(most_occurring_letter)

#for print 2 or more letters have same count

list=[] 
for i in d:
    if d[i]==most_occurring:
        list.append(i)
print(list)
