low=int(input("Enter lower range :"))
high=int(input("Enter upper  range :"))

for i in range(low,high+1):
  if (i >1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
     print(i,end=",")
 