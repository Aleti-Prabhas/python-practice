list1=[]
m,n=input("enter the dimensions of matrix:").split()
for i in range(0,int(m)):
    li=list(map(int,input().split()))[:int(n)]
    list1.append(li)
print(list1)


def finding_element(ele):
    for i in range(0,int(m)):
        if ele in list1[i] :
            return True
    return False
    
element=int(input("enter the element u want to find from the matrix:"))
print(finding_element(element))
