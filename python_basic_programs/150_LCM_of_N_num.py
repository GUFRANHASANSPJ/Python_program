def LCM_of_2_Num(num1,num2):
    lcm=num1
    i=1
    while True:
        if lcm%num1==0 and lcm%num2==0:
            return lcm
        i+=1
        lcm=num1*i
        
arr=[1,2,3,4,5,6]
lcm=arr[0]
for i in range(len(arr)):
    lcm=LCM_of_2_Num(arr[i],lcm)
    print(lcm)

        
        
