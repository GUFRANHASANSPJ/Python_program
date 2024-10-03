a=[-1,6,5,5,-10,6]
m1,m2,m3=0,0,0
for i in a:
    if i>m1:
        m1,m2,m3=i,m3,m1

    elif i>m2 and i<m1 and i>m3:
        m2,m3=i,m2

    elif i>m3 and i<m1 and i<m2:
        m3=i
print(m1,m2,m3