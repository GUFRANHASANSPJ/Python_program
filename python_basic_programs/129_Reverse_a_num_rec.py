def reverse(num,rev=0):
    if num==0:
        return rev
    r=num%10
    rev=rev*10+r
    return reverse(num//10,rev)
print(reverse(12345))