# def check_pow_2(a):
#     if a<2:
#         return False
#     while a!=1:
#         if a%2!=0:
#             return False
#         a=a//2
#     return True
# a=int(input())
# print(check_pow_2(a))
    
inp=int(input("Enter number:"))
x=False
for i in range(1,inp):
    res=2**i
    if res==inp:
        x=True
        break
        
if x==True:
    print(True)
else:
    print(False)    