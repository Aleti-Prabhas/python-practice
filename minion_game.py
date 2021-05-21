input_string=input()
kevin=0
stuart=0

vowels=['a','e','i','o','u']



def sub_string(string):
   sub_string_set=[]
   for i in range(0,len(string)):
      for j in range(i,len(string)):
         sub=string[i:j]
         sub_string_set.append(sub)
   print(sub_string_set)    
   return sub_string_set



sub=sub_string(input_string)
for i in range(0,len(sub)):
   if(str(str[i])!=""):
      if(str(sub[i]).startswith('a') or str(sub[i]).startswith('e') or str(sub[i]).startswith('i') or str(sub[i]).startswith('o') or str(sub[i]).startswith('u')):
         kevin=kevin+1
      else:
         stuart=stuart+1


if kevin>stuart:
   print("kevin",kevin)
else:
   print("stuart",stuart)