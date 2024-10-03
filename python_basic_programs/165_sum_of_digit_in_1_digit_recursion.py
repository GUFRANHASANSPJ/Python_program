N=98
def sum_of_digit(N):
    sum=0
    if 0<N<10:
        return N
    while N!=0:
        r=N%10
        sum+=r
        N=N//10
    return sum_of_digit(sum)
print(sum_of_digit(N))
    
        

