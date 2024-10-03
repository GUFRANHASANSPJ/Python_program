def chech_M(arr,sarr):
    idx=0
    maxx=0
    for i in sarr:
        for j in range(len(arr)):
            if i==arr[j]:
                idx=j
        if idx>=maxx:
            maxx=idx
        else:
            return False
    return True           
arr=[2,4,6,7,8,9,5]
sarr=[2,6,4]
print(chech_M(arr,sarr))