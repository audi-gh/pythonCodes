#!/usr/bin/env python
# coding: utf-8

# In[30]:


import math
od=[]
ed=[]
d,ds=0,0
s,w=0,0
cardno=input("enter credit card number")
checkDigit=int(cardno[-1])

for i in range(0,15):
    
    if(i%2==0):
        od.append(int(cardno[i]))
    else:
        ed.append(int(cardno[i]))
print(od)
                  
for j in range(0,len(od)):
    od[j]=od[j]*2
    w=od[j]
    while(w!=0):
        d=w%10
        ds+=d
        w=w//10
    od[j]=ds
    ds=0
print(od)
print(ed)
s=sum(ed)+sum(od)
if((s+checkDigit)%10==0):
    print("Valid credit card number ")
                  
else:
    print("Not a valid credit card number number")
                  
    


# In[ ]:




