a=8
for i in range(1,int(a**0.5+10)):
    for j in range(2,int(a**0.5+10)):
        if i**j==a:
            print(1)
            break

