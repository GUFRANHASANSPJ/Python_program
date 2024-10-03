def search(X,Y):
    idx=0
    l=len(Y)
    for i in range (len(X)):
        if X[i]==Y[0]:
            if X[i:l+i]==Y:
                idx=i+1
    if idx :
        return idx
    return idx
			
X = "geeksforgeeks"
Y = "geeks"
print(search(X,Y))
      