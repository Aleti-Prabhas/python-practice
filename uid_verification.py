def seperation(uid):
    digits=[]
    upper=[]
    lower=[]
    counter=0
    for i in range(0,10):
        if(uid[i].isdigit()):
            if(uid[i] not in digits):
                 digits.append(uid[i])
            
        elif(uid[i].isupper()):
            if(uid[i] not in upper):
                upper.append(uid[i])
            
        elif(uid[i].islower()):
            if(uid[i] not in upper):
                lower.append(uid[i])
        else:
            counter=counter+1
    return digits,upper,lower,counter

n=int(input())
for i in range(0,n):
    uid1=input()
    if len(uid1)==10 :
        digits,upper,lower,counter=seperation(uid1)
        lat=digits+upper+lower
        if(len(digits)>=3 and len(upper)>=2 and counter==0 and len(lat)==10):
            print("valid")
        else:
            print("invalid")  







    
    
        
    
                 
