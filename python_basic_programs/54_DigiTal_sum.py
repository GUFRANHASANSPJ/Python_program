def digital_sum(n):
    if n=="0":
        return 0
    ans=0
    for i in n:
        ans=(ans+int(i)) % 9
    if ans==0:
        return 9
    else:
        return ans % 9
a=input()
print( digital_sum(a) )
    
