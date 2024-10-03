def sum_of_numbers(num,sum=0):
    if num==0:
        return sum
    
    r=num%10
    sum=sum+r
    num=num//10
    return sum_of_numbers(num,sum)
print(sum_of_numbers(123))
