def Lcm_of_2_num(num1,num2):
    lcm=num1
    while True :
        if lcm%num1==0 and lcm%num2==0:
            return lcm
        lcm+=num1
'''2/5 +3/8'''
n1=2 ; n2=3
d1= 5; d2=8
lcm_of_d1_and_d2=Lcm_of_2_num(d1,d2)
N=((lcm_of_d1_and_d2 //d1) *n1)+ ((lcm_of_d1_and_d2 // d2)*n2)
D=lcm_of_d1_and_d2
print(N,'/',D)