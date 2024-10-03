def minStep( H, U, D):
    # code here
    c=U-D
    ct=0
    while True:
        H=H-c
        ct+=1
        if H<=U:
            return ct+1
print(minStep(10,4,1)