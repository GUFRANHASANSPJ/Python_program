def Hcf_2_num(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1
'''2/5 +3/8'''
'''Cross Multiplication and sum'''
n1=384 ; n2=778
d1= 887; d2=916

if d1==d2:
    print(n1+n2,'/',d1)
else:
    N=n1*d2+ n2*d1
    D=d1*d2
''' To change into simplest form '''
sim=Hcf_2_num(N,D)
print(N//sim,'/',D//sim)
