def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range((n-i-1)):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1]=arr[j+1],arr[j]

a=[25,25,46,64,4,78,-1]
bubble_sort(a)
# for i in range(len(a)-1):
#     if a[i]==a[i+1]:
#         continue
#     else:
#         print(a[i],end=" ")
# print(a[-1])
print(a)