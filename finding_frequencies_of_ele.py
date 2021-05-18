n=int(input())
arr=list(map(int,input().split()[:n]))
my_dict={}
for ele in arr:
    if ele not in arr:
        my_dict[ele]=1
    else:
        my_dict[ele] 

for i in my_dict:
    print(i," ",my_list[i])