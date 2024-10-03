arr= [7, 98, 56, 43, 45, 23, 12, 8,567]
k=54
'''ans  should be less than 54 also diff = 1'''
out=[43,45 ,23,12]
t=''
temp=[]
for i in arr:
    if len(str(i))!=1 and i<5412:
        for j in range ( len(str(i))-1 ):
            if int(str(i)[j]) - int(str(i)[j+1]) ==1 or int(str(i)[j]) - int(str(i)[j+1]) ==-1:
                t=True
            else:
                t=False
                break
        if t==True:
            temp.append(i)
print(temp)




            



