n=int(input("Enter num:"))
def is_power(n):
    for i in range(n):
        for j in range(n):
            if j**i==n:
                return "Yes"
    return "No"
    
print(is_power(n))