a=5
b=6

print("The value of a and b before swapping is ",a,b)
# with a temp variable
# temp=a
# a=b
# b=temp

#  without using a temp variable using addition method 
# a=a+b
# b=a-b
# a=a-b

# using mul method
a=a*b
b=int(a/b)
a=int(a/b)
print("The value of a and b after  swapping is ",a,b)
