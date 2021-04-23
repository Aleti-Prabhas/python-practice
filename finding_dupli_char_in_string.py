string1=input("enter the string : ")
duplicates = []
for char in string1:
    if string1.count(char)>1:
        if char not in duplicates:
            duplicates.append(char)
print("the no duplicate characters are:",len(duplicates))
print("the characters that have duplicates are :",duplicates)
