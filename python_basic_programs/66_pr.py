a="Hh$e#21!Eo@34L5L?O6^"
out="HELLOhello23456$#!@?^"
tempA=""
tempa=""
temp1=""
tempsp=""
for i in a:
     if ('A'<=i<='Z') ==True:
          tempA+=i
     elif ('a'<=i<='z') ==True:
          tempa+=i
     elif i in "0123456789":
          temp1+=i
     else:
          tempsp+=i
     
print(tempA+tempa+temp1+tempsp)
          