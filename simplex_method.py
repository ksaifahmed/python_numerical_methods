# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:17:53 2019

@author: home
"""

import numpy as np
import matplotlib.pyplot as plt

#taking input
file = open("in2.txt","r")
line = str(file.readline())
arr1 = np.array((line.split(" ")))
varno = arr1.size
lines = file.readlines()
constr = 0
for line in lines:
    constr += 1
file.close()
    
#creating the matrix table
M = np.zeros(shape=(constr+1,constr+varno+3))
r,c = M.shape
c -= 1

#setting values
slkcount = 1
for i in range(0,r-1):
    arr = np.array(lines[i].split(" "))
    for j in range(0,varno):
        M.itemset((i,j),float(arr[j]))
    M.itemset((i,j+slkcount),1.0)
    M.itemset((i,c-1),float(arr[j+1]))
    slkcount += 1

for i in range(0,varno):
    M.itemset((r-1,i),float(arr1[i])*-1.0)
M.itemset((r-1,c-2),1.0)

str1 = ["" for x in range(varno+constr+3)]
str2 = ["" for x in range(constr+1)]


for i in range(0,varno):
    str1[i] = "x"+str(i+1)
for i in range(varno,varno+constr):
    str1[i] = "S"+str(i-1)
id = varno+constr
str1[id] = "Z"
id += 1
str1[id] = "Sol"
id += 1
str1[id] = "intercept"
for i in range(0,constr):
    str2[i] = "S"+str(i+1)
str2[constr] = "Z"
print(str2)




def printer(M):
    r,c = M.shape
    print("Basic",end="\t")
    for col in range(0,c):
        print(str1[col],end="\t")
    print()
    for row in range(0,r):
        print(str2[row],end="\t")
        for col in range(0,c):
            print("%0.4f"%M.item((row,col)),end="\t")
        print()
    print(end="\n")



print("Initial Table: ")
printer(M)
print()




def optimal(M):
    flg = 0
    r,c = M.shape
    c -= 1
    for col in range(0,c):
        if M.item((r-1,col)) >= 0.0:
            flg += 1
    if flg == c:
        return True
    return False

def minim(M):
    r,c = M.shape
    c -= 1
    cidx = 0
    Min = M.item((r-1),0)
    for col in range(1,c-1):
        if M.item((r-1,col)) < Min:
            Min = M.item((r-1,col))
            cidx = col
    return cidx

def leastRat(M,cidx):
    r,c = M.shape
    c -= 1
    div = M.item((0,cidx))
    if div != 0.0:
        Min = M.item((0,c-1))/div
    else:
        div = 0.0000000000001
        Min = M.item((0,c-1))/div
    M.itemset((0,c),Min)
    ridx = 0
    for row in range(1,r-1):
        div = M.item((row,cidx))
        if div != 0.0:
            tmp = M.item((row,c-1))/div
        else:
            div = 0.0000000000001
            M.item((row,c-1))/div
        M.itemset((row,c),tmp)
        if tmp < Min:
            Min = tmp
            ridx = row
    return ridx
    
def divideCol(M,row,val):
    r,c = M.shape
    c -= 1
    for col in range(0,c):
        M.itemset((row,col),M.item((row,col))/val)
    return M
 
    
def rowsub(A,r1,r2,Lfactor):
    j,k = A.shape
    k -= 1
    for col in range(0,k):
         tmp = A.item((r1,col))-A.item((r2,col))*Lfactor
         A.itemset((r1,col),tmp)
    return A


            

r,c = M.shape   
c -= 1
itr = 1
while optimal(M)==False:
    kcol = minim(M)
    krow = leastRat(M,kcol)
    str2[krow] = str1[kcol]
    print("Iteration:",itr)
    print("pivot row: ",krow,",pivot column: ",kcol)
    print("Intercept calculated:")
    printer(M)
    M = divideCol(M,krow,M.item((krow,kcol)))
    print("After pivot row division:")
    printer(M)

    
    for row in range(0,r):
        if row == krow:
            continue
        if M.item((row,kcol)) != 0.0:
            val = M.item((row,kcol))/M.item((krow,kcol))
            M = rowsub(M,row,krow,val) 
    itr += 1
    print("After elimination of other pivot column elements:")
    printer(M)                         



print("Final Table:")
printer(M)


print("Maximum is: ",M.item((r-1,c-1)))  
print("Corresponding values: ")
for i in range(0,varno):
    flg = 0
    for j in range(0,constr):
        if str1[i] == str2[j]:
            print(str1[i],"=",M.item((j,c-1)))
            flg = 1
    if flg == 0:
        print(str1[i],"=",0.0)
          
























































  



























  
