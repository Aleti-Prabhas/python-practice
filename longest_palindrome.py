string=input("enter the string : ")

def palindrome1(string1):
    palin_list=[]
    palin_len_list=[]
    for i in range(0,len(string1)):
        for j in range(i+1,len(string1)):
            palin=string1[i:j]
            palin1=palin[::-1]
            if(palin1==palin):
                palin_list.append(palin)
                palin_len_list.append(len(palin))
    max_val=max(palin_len_list)
    maxi1=palin_len_list.index(max_val)
    print(palin_list[maxi1]) 

palindrome1(string)             
                   
                
  