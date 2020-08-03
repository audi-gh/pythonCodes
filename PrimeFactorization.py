# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:25:36 2020

@author: Win10
"""


n=int(input("enter the number"))
c=0
l=[]
if(n%2==0):
    l.append(2)
for i in range(3,n):
    if(n%i==0 and i%2!=0):
        l.append(i)
for i in range(0,len(l)):
    print(l[i])
    


    
   
    
    
    