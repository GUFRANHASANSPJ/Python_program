'''
[[2 3 4]
 [5 6 8]
 [7 8 9]]
'''
mat1=[]
n=3
# for i in range(n):
#     ins=[]
#     for j in range(n):
#         ins.append(int(input((f'Enter the {j}th element: '))))
#     mat1.append(ins)
# print(mat1)
# print sum of its left diagonals
mat1=[[2, 3, 4], [5, 6, 8], [7, 8, 9]]
lftsum=0
rtsum=0
for i in range(len(mat1)):
    lftsum+=mat1[i][i]
    rtsum+=mat1[i][len(mat1)-(i+1)]
print(lftsum)
print(rtsum)


