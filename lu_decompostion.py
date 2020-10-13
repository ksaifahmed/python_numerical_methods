# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:45:49 2019

@author: home
"""

import numpy as np
import sys

A1=np.matrix('25.,6.,1.,7.;64.,15.,3.,5.;144.,20.,10.,4.;20.,30.,60.,1.')
A2 = np.matrix('25.,5.,1.;64.,8.,1.;144.,12.,1.')



#taking inputs
file = open("in1.txt","r")
n = int(file.readline())


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

print(A)  
file.close()


#absolute maximum of col
def amax(A, col):
    j,k = A.shape
    max = abs(A.item((0,col)))
    idx = 0
    for i in range(1,j):
        if max < abs(A.item((i,col))):
            idx = i
            max = abs(A.item((i,col)))
    return max,idx




#swap rows for pivoting
def swapRow(A,r1,r2):
    j,k = A.shape
    for col in range(0,j):
        temp = A.item((r1,col))
        A.itemset((r1,col),A.item((r2,col)))
        A.itemset((r2,col),temp)
    return A
        




#row subtraction
def rowsub(A,r1,r2,Lfactor):
    j,k = A.shape
    for col in range(0,j):
         tmp = A.item((r1,col))-A.item((r2,col))*Lfactor
         A.itemset((r1,col),tmp)
    return A



#declaring L
j,k = A.shape
L = np.zeros(shape=(j,k))
L = np.asmatrix(L)
for i in range(0,j):
    L.itemset((i,i),1)


#decomposition 
for col in range(0,j-1):
    for row in range(col+1,k):
        if A.item((row,col))!=0.0 and A.item((col,col))!=0.0:
            l = A.item((row,col))/A.item((col,col))
            L.itemset((row,col),l)
            A = rowsub(A,row,col,l)


#answer of L
print(L)
print()

#answer of U
print(A)


f = open("out1.txt","w+")
def write(L,precsn):
    r,c = L.shape
    for i in range(0,r):
        for j in range(0,c):
            ans = float(L.item((i,j)))
            f.write(str(round(ans,precsn)))
            if j < c-1:
                f.write(" ")
        f.write("\n")


write(L,4)
f.write("\n")
write(A,4)
f.write("\n")



#unique solution checker
flg = 0
for i in range(0,n):
    counter = 0
    for j in range(0,n):
        if A.item((i,j)) == 0.0:
            counter += 1
    if counter == 3.0:
        flg = 1
        break
if flg == 1:
    f.write("No unique solution")
    f.close()
    sys.exit()
    


#A = rowsub(A,1,0,2.56)
#A = rowsub(A,2,0,5.76)
#A = rowsub(A,3,0,0.8)


#for col in range(0,j-1):
#    m,ridx = amax(A,col)
#    if m > abs(A.item((col,col))):
#        A = swapRow(A,ridx,col)
#        temp = ans.item((ridx,0))
#        ans.itemset((ridx,0),ans.item(col,0))
#        ans.itemset((col,0),temp)


        
#finding Y
Y = np.zeros(shape=(n,1))
for i in range(0,n):
    tmp = B.item(i)
    for j in range(0,i):
        tmp -= (L.item((i,j))*Y.item(j,0))
    Y.itemset(i,tmp)    

print()
print(Y)    
    
#finding X
X = np.zeros(shape=(n,1))
for i in np.arange(n-1,-1,-1):
    i = int(i)
    tmp = Y.item(i)
    for j in np.arange(n-1,i,-1):
        j = int(j)
        s1 = (A.item(i,j)*X.item(j,0))
        tmp -= s1
    tmp /= A.item((i,i))
    X.itemset(i,tmp)

print()
print(X)


write(Y,2)
f.write("\n")
write(X,2)

f.close()




































