print("signup")
users={}
a=int(input("Number of users"))
for i in range(a):
    isSpammer = False
    username=input("Enter a user name")
    c = 1
    while username in users:
        
        if c == 3:
            isSpammer = True
            break
        username=input("Re-enter a user name")
        c = c + 1 #2
    if isSpammer:
        break
    password=input("Enter pssword")
    users[username]=password
print(users)
print("Login")
user_name =input("Enter user name:")
if user_name in users:
    password1=input("Enter your password")
    correct_psssword = users[user_name]
    if password1== correct_psssword:
        print("Login successful")
    else:
        print("your password is wrong")
else:
    print("your user name is wrong")

