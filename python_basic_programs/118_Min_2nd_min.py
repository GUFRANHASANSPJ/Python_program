
def min(a):
    m1=m2=float('inf')
    if len(a)<2:
        return -1
    for i in a:
        if i<m1:
            m1,m2= i,m1
        elif i<m2 and i>m1:
            m2=i
    return m1,m2
a=[1,1,2,2,3,3,-1,-1]
print(min(a))

# import math

# arr = [2,2,2,6]
# first = second = math.inf
# print(first)

# for i in range(0, len(arr)):
#   if arr[i] < first:
#     second = first
#     first = arr[i]

#   elif (arr[i] < second and arr[i] != first):
#     second = arr[i]

# print(second)
# print(first)

# a=[-16,2,-14,9,7,2,6,4,3,-17,-15,-8,-2]

