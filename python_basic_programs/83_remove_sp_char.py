a="hi_how r YOU$and What*you_doing"
temp=""
for i in a:
    if i.isalpha()==False :
        temp+=" "
    else:
        temp+=i
print(temp.capitalize())
