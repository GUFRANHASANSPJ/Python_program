def calculator( a, b,c,d,inp):
    if inp=="+":
        print(a+b+c+d)
    elif inp=='-':
        print(a-b-c-d)
    elif inp=='*':
        print(a*b*c*d)
    elif inp=='/':
        print(a/b/c/d)
a=int(input())
b=int(input())
inp=input("select any one: + - * / ")
calculator(a,b,inp)
