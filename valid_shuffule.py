string1=input("enter the string 1 :")
string2=input("enter the string 2 :")
shuffled_string=input("enter the shuffuled mix string :")
mixed_string=string1+string2
final_string=""
if(len(mixed_string)==len(shuffled_string)):
    for char in mixed_string:
        if(char in shuffled_string):
            shuffled_string=shuffled_string.replace(char,'',1)
            print(shuffled_string)
    if(shuffled_string==""):
        print("YES ,the string is  a shuffle mix of other 2 string")
    else:
        ("NO, the string is not a shuffle mix of other 2 strings")
else:
    print("NO, the string is not a shuffle mix of other 2 strings")

