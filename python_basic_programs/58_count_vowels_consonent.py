# a=input()
a="aeoui"
dic={"vowels":0,"consonent":0}
vowels="aeoui"
for i in a:
    if i in vowels:
        dic["vowels"]+=1
    else:
        dic["consonent"]+=1
print(dic)


