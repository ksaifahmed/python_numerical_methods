# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:52:05 2019

@author: home
"""
import numpy as np








file = open("in1.txt","r")
n = int(file.readline())
print(type(n))

A = np.zeros(shape=(n,n))
B = np.zeros(shape=(n,1))
for i in range(0,n):
    line = str(file.readline())
    a = np.array(line.split(" "))
    for j in range(0,n):
        A.itemset((i,j),float(a[j]))
        
for i in range(0,n):
    tmp = float(file.readline())
    B.itemset(i,tmp)

file.close()   
    
    
    
    
    
    
    
    
    
    
    
