def check_sub_string(str,sub_str):
    L=len(sub_str)
    for i in range(len(str)):
        if str[i:i+L]==sub_str:
            return i
    return -1

str="geeksforgeeks"
sub_str='geeks'
a=check_sub_string(str,sub_str)
if a!=-1:
    print(sub_str,"is present at",a,"th index")
else:
    print(sub_str,"is not Present in ",str)
            

