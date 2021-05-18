def binary_search(my_list,target):
    left=0
    right=len(my_list)-1
    while left<=right:
        middle=(left+right)//2
        if target==my_list[middle]:
            return middle
        elif target>=my_list[middle]:
            left=middle+1
        else:
            right=middle-1
    return -1

x=binary_search([1,2,3,4,5,6,7,8,9],1)
print(x)