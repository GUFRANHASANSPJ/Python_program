# a=input()
a="programming language"
output="prOgrAmmIng lAngUAgE"
alphabet="aeouiAEOUI"
temp=""
for i in a:
    if i in alphabet:
        temp+=chr( ord(i)-32 )
    else:
        temp+=i
print(temp)