nums = [7,2, 4, 5, 9, 7]
nums.sort()
arr=[]
for i in range(len(nums)-1):
    diff=abs(nums[i]-nums[i+1])
    arr.append(diff)
print(arr)
    