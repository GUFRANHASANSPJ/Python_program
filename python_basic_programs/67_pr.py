def test(tem):
    if tem[0]!="#" and len(tem)!=7:
        return False
    tem=tem[1::]
    for i in tem:
        if (('a'<=i<='f' or 'A'<=i<='F') or (i in "0123456789"))==False:
            return False
    return True
a=input()
if test(a)==True:
    print("true")
else:
    print("false")