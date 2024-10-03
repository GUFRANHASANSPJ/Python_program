nums = [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1]
Output=3
maxe=0
ct=0
for i in nums:
    if i==1:
        ct+=1
    else:
        if ct>maxe:
            maxe=ct
            ct=0
        else:
            ct=0
if ct>maxe:
    maxe=ct
print(maxe)
