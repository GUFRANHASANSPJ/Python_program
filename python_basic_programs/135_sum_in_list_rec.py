def find_sum(arr,sum=0,i=0):
    if  i== len(arr):
        return sum
    
    if type(arr[i])==int:
        sum+=arr[i]
        return find_sum(arr,sum,i=i+1)
    
    elif type(arr[i])==list :

        return find_sum(arr[i],sum,i=0)

arr=[2,5,[ 5,6,[5,9,8,1,1] ] ]
print(find_sum(arr))
