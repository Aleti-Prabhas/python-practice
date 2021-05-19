n,max1=input().split(" ")
list1=list(map(int,input().split()[:int(n)]))
list1.sort()
counter=0
while list1[0]<=int(max1):
    counter=counter+1
    val=list1[0]+list1[1]*2
    list1.remove(list1[0])
    list1.remove(list1[1])
    list1.append(val)
    

print(counter)