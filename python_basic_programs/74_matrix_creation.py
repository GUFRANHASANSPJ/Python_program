a=int(input())
b=int(input())
matrix=[]

for i in range(a):
    d=[]
    for j in range(b):
        d.append(int(input()))
    matrix.append(d)
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()

  