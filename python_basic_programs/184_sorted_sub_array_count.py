def sortedCount(Mat):
    ct=0
    desc=False
    asc=False
    for i in Mat:
        for j in range(len(i)-1):
            if i[0]<i[1]:
                desc=False
                if i[j]<i[j+1]:
                    asc=True
                else:
                    asc=False
                    break

            elif i[0]>i[1]:
                asc=False
                if i[j]>i[j+1]:
                    desc=True
                else:
                    desc=False
                    break
        if asc==True:
            ct+=1
        elif desc==True:
            ct+=1
        
    return ct
Mat=[ [1,2,3],[6,5,4],[7,9,8] ,[6,9,4]]
print(sortedCount(Mat))