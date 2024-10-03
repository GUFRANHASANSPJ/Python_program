N=871
while N>9:
    rem=N%10
    N=N//10
    sum=rem+N
    N=sum
print(N)
