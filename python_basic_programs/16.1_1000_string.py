a=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
b=["Ten","Eleven","Tweleve","Thirteen","Fourteen","Fifteen","Sixteen","Seventen","Eighteen","Nineteen"]
c=["Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
d=["One Hundred","Two Hundred","Three Hundred","Four Hundred","Five Hundred","Six Hundred",
   "Seven Hundred","Eight Hundred","Nine Hundred",]

num=int(input())
if 0<=num<=9:
    oness=a[num]
    print(oness)

elif 10<=num<=19:
    tenss=b [num%10]
    print(tenss)

elif 20<=num<=99:

    tens=(num//10)-2
    ones=(num%10)
    print(c[tens],a[ones])
# else:
#     print("Greater than hundred or neagtive")

elif 100<=num<=999:
    Hundred=(num//100)-1

    num=num%100
    if 0<=num<=9:
        oness=a[num]
        print(d[Hundred],oness)

    elif 10<=num<=19:
        tenss=b [num%10]
        print(d[Hundred],tenss)

    
    elif 20<=num<=99:

        tens=(num//10)-2
        ones=(num%10)
        print(d[Hundred],c[tens],a[ones])

else:
    print("Greater than Thousand or neagtive")
    
