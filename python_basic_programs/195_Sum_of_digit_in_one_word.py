def sum_digit(N):
    sum=0
    while N:
        r=N%10
        sum+=r
        N=N//10
    if sum <10:
        return sum
    else:
        N=sum
        return sum_digit(N)
    
print(sum_digit(123566))