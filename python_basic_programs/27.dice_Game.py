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
dice=(1,2,3,4,5,6)
dicepic=(a,b,c,d,e,f)
if r in dice:
     if r in(2,3):
        print("You got",r)
        print(dicepic[r-1])
        score=r*1
        print("Yor score is:",score)
     elif r in (4,5):
           print("You got",r)
           print(dicepic[r-1])
           score=r*2
           
           print("Yor score is:",score)  
     elif r==1:
          print("You got",r)
          print(dicepic[r-1])
          score=r*0
          print("Yor score is:",score)
     elif r==6:
           print("You got",r)
           print(dicepic[r-1])
           score=r*2
           print("Yor score is:",score)
           print("You Have Earned One more Change To Play!")
           s=random.randint(1,5)
           print("Again You got",s)
           print(dicepic[s-1])
           print("Your Total score is:",score+s*2)

          

   