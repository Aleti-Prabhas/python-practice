#string=input()
#list1=string.split()
#list2=[]
#for char in list1:
#    x=char.capitalize()
 #   list2.append(str(x))
#print(*list2)


s=input()
for x in s[:].split():
    s=s.replace(x,x.capitalize())
print(s) 