import random
r=random.randint(1,6)
a='''
     ------    
    |  1   | 
    |      |
     ------ 
     '''
b='''
     ------
    |  2   | 
    |      |
     ------ 
     '''
c='''
     ------
    |  3   | 
    |      |
     ------ 
     '''
d='''
     ------
    |  4   | 
    |      |
     ------ 
     '''
e='''
     ------
    |  5   | 
    |      |
     ------ 
     '''
f='''
     ------
    |  6   | 
    |      |
     ------ 
     '''
if r==1:
    print(a)
    print("You Got ",r*0,"Chocolate")
elif r==2:
    print(b)
    print("You Got ",r,"Chocolate")

elif r==3:
    print(c)
    print("You Got ",r,"Chocolate")

elif r==4:
    print(d)
    print("You Got ",r*2,"Chocolate")

elif r==5:
    print(e)
    print("You Got ",r*2,"Chocolate")

elif r==6:
    print(f)
    print("You Got ",r*2,"Chocolate")
    print("You Got 1 Change to play")
    total=r*2
    f=random.randint(1,5)
    if f==1:
        print(a)
        print("You Got ",f*0 +total,"Chocolate")
    elif f==2:
        print(b)
        print("You Got ",f*1 +total,"Chocolate")
    elif f==3:
        print(c)
        print("You Got ",f*1 +total,"Chocolate")
    elif f==4:
        print(d)
        print("You Got ",f*2 +total,"Chocolate")
    elif f==5:
        print(e)
        print("You Got ",f*2 +total,"Chocolate")


