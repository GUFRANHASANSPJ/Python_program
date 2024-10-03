username="gufran531"
password="Gufran531"
a=input("Enter the username:")
b=input("Enter the password:")
if a==username and b==password:
    print("LOGIN SUCCESFULL")
elif a==username:
    if b!=password:
        print("INVALID PASSSWORD")
elif a!=username:
    if b==password:
        print("INVALID CREDENTIALS")
else:
    print("Invalid username and password")
    

    
        