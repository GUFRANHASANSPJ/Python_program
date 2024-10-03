low=int(input("Enter the lower range :"))
upper=int(input("Enter the upper range :"))

for i in range(low,upper+1):
  size=len(str(i))
  temp=i
  sum=0
  
  while(temp!=0):
    digit=temp%10
    sum=sum+pow(digit,size)
    temp=temp//10
  if (sum==i):
     print(i,end=",")
