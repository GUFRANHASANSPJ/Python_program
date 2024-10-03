dict={1:["jan",31],2:["feb",28],3:["mar",31],4:["apr",30],5:["may",31],6:["jun",30],7:["july",31],8:["aug",31],9:["sep",30],9:["sep",31],10:["oct",31],11:["nov",30],1:["dec",31]

}
a=int(input ("enter :"))
if a in dict:
    print("it is month of ",dict[a][0], "and it has ",dict[a][1],"days")

else:
    print("invaslid ")
