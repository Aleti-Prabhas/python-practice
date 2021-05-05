list1=[]
m,n=input("enter the dimensions of matrix:").split()
for i in range(0,int(m)):
    li=list(map(int,input().split()))[:int(n)]
    list1.append(li)
print(list1)

for i in range(0,int(n)):
    for j in range(int(m)-1,-1,-1):
        print(list1[j][i],end="  ")