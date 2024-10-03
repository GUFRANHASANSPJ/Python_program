print("\t***Welcome To****\n *****Gufran-Hasan pizza-House**** ")
pizza={1:["Margaritha",100] ,2:["Chicken pizza",200], 3:["Non Veg loaded",300],
       4:["Corn pizza",400],5:["Garlic",500]}

addon={1:["Coke",10],2:["Sweet",20],3:["mayonese",30],4:["Extra cheese",40]}

order=int(input('''Please Select Your Pizza!
            1. Margaritha     Rs 100
            2. Chicken pizza  Rs 200
            3. Non Veg loaded Rs 300
            4. Corn pizza     Rs 400
            5. Garlic pizza   Rs 500\n
            ****Please Select Any One Pizza!*****\n'''))
totalbill=0
if 1<=order<=5:
    quantity=int(input("Please Select the Quantity:"))
    print(f'''You Have selected : {pizza[order][0]}
The Quantity of {pizza[order][0]} is:{quantity}''')
    
    totalbill=totalbill+pizza[order][1]*quantity
    print(f"Your Bill is Rs {totalbill} ")

    a=int(input('''Do You Want Addon?\n Press 1 For Yes\n press 0 For No'''))
    if a==1:
        print('''Please Select Any One:
                1. coke     Rs 10
                2. sweet    Rs 20
                3. Mayonese Rs 30
                4. Extra Cheese  Rs 40''')
        adn=int(input("Please Select Any One "))
        if 1<=adn<=4:
            print(f'''You Have Selected {addon[adn][0]}  ''')
            aq=int(input (f"Enter The Quantity of {addon[adn][0]}: "))
            print(f'''Your Item is :{quantity} {pizza[order][0]} and {adn} {addon[a][0]} ''')
    
            print("\n")
            print("Your Total Bill Is", totalbill+ (addon[adn][1]*aq) )
        
        else:
            print("Invalid Choice")
    else:
        print("Your Total bill is Only :",totalbill)
else:
    print("Invalid Selection")


                
                