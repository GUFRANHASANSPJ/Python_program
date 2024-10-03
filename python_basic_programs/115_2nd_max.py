def secnd_max(a):
    m1=m2=float('-inf')
    for i in range(len(a)):
        if len(a)<2:
            return -1
        
        if a[i]>m1:
            m2=m1
            m1=a[i]
        elif a[i]!=m1 and a[i] >m2:
            m2=a[i]
    if m2==float('-inf'):
        return -1   
    return m1,m2
a=[-2,-9,-10]
print(secnd_max(a))
