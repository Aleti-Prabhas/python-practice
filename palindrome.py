string=input("enter the string :")
palindrome = string[::-1]
if(string == palindrome):
    print("the given word is a palindrome")
else:
    print("the given word is not a palindrome")