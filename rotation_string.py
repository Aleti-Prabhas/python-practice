string1=input("enter the string:")
string2=input("enter the rotation of string :")
def rotation_check(str1,str2):
    for i in range (0,len(str1)):
        if(len(str1)!=len(str2)):
            return False
        else:
            pass_string=str1+str1
            if str2 in pass_string:
                 return True
            else:
                 return False
    
answer=rotation_check(string1,string2)
print(answer)