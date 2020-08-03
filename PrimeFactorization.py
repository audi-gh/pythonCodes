# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:25:36 2020

@author: Win10
"""
#I have extracted all the prime factors and appended them into a list
#Since 2 is the only even prime number we have considered it seperately


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


    
   
    
    
    
