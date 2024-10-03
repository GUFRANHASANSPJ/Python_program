A = "geeksforgeeks"
B = "geeksquiz"
tem=''
for i in A :
    if i not in B and i not in tem:
        tem+=i

for j in B:
    if j not in A and j not in tem:
        tem+=j
print("".join(sorted(tem)))
        
