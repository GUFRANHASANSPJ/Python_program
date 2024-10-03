a=float(input("Enter the Number:"))
i=input('''Which Operation Do you Want\n
        +  -  *  %  /  //
        ''')
if i in ("+","-","*","/","//","**"):
    b=float(input("Enter The second Number:"))
    if i=="+":
        print(f"The sum of {a} and {b} is {a+b}")
    elif i=="-":
        print(f"The subtraction of {a} and {b} is {a-b}")
    elif i=="*":
        print(f"The Multiplication of {a} and {b} is {a*b}")
    elif i=="/":
        print(f"The Division of {a} and {b} is {a/b}")
    elif i=="//":
        print(f"The Floordivision of {a} and {b} is {a//b}")
    elif i=="**":
        print(f"The Power of {a} and {b} is {a**b}")
else:
    print("Invalid selection:")

