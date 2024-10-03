def shortest_palindrome(inp):
    tem=inp
    for i in range(1,len(tem)+1):
        if inp==inp[::-1]:
            return inp
        else:
            inp=tem[-i]+inp
    return -1
inp='defes'
out='efedefe'
print(shortest_palindrome(inp))