def rang(num,sum=0):
    if num==0:
        return sum
    sum+=num
    return rang(num-1,sum)

# num=int(input("Enter The range:"))
print(rang(5))