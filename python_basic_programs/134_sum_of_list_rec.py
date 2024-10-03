def find_sum(arr,sum=0):
    if  not arr:
        return sum
    sum+=arr[0] 
    arr.remove(arr[0])
    return find_sum(arr,sum)


# arr=[2,5,[ 5,6,[5,9,8] ] ]
crr=[2,4,6]
print(find_sum(crr))
