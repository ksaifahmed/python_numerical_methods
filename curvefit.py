# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:39:38 2019

@author: home
"""

import numpy as np
import matplotlib.pyplot as plt

file = open("data.txt","r")
lines = file.readlines()
xcor = []
ycor = []
cornum = 0


for line in lines:
    x, y = (line.split(" "))
    xcor.append(float(x))
    ycor.append(float(y))
    cornum += 1

plt.figure(1)
plt.scatter(xcor,ycor,0.9)
   
sumx = sumx2 = sumx3 = sumx4 = sumx5 = sumx6 = sumy = sumxy = sumx2y = sumx3y = 0.0
for i in range(0,cornum):
    sumx += xcor[i]
    sumx2 += (xcor[i]**2)
    sumx3 += (xcor[i]**3)
    sumx4 += (xcor[i]**4)
    sumx5 += (xcor[i]**5)
    sumx6 += (xcor[i]**6)
    sumy += ycor[i]
    sumxy += (xcor[i]*ycor[i])
    sumx2y += ((xcor[i]**2)*(ycor[i]))
    sumx3y += ((xcor[i]**3)*(ycor[i]))

Min = xcor[0]
Max = xcor[0]
for i in range(1,cornum):
    if xcor[i] > Max:
        Max = xcor[i]
    if xcor[i] < Min:
        Min = xcor[i]
    
fomat = np.zeros(shape=(2,2))
foans = np.zeros(shape=(2,1))
fomat.itemset(0,cornum)
fomat.itemset(1,sumx)
fomat.itemset(2,sumx)
fomat.itemset(3,sumx2)
foans.itemset(0,sumy)
foans.itemset(1,sumxy)
fosol = np.linalg.solve(fomat,foans)
x1 = np.arange(Min,Max,0.1)
y1 = fosol.item(0) + fosol.item(1)*x1
plt.plot(x1,y1,color="orange", linewidth = "2.2", label="first order")

somat = np.zeros(shape=(3,3))
soans = np.zeros(shape=(3,1))
somat.itemset(0,cornum)
somat.itemset(1,sumx)
somat.itemset(2,sumx2)
somat.itemset(3,sumx)
somat.itemset(4,sumx2)
somat.itemset(5,sumx3)
somat.itemset(6,sumx2)
somat.itemset(7,sumx3)
somat.itemset(8,sumx4)
soans.itemset(0,sumy)
soans.itemset(1,sumxy)
soans.itemset(2,sumx2y)
sosol = np.linalg.solve(somat,soans)
y2 = sosol.item(0) + sosol.item(1)*x1 + sosol.item(2)*(x1**2)
plt.plot(x1,y2, color = "crimson", linewidth="2", label="second order")

tomat = np.zeros(shape=(4,4))
toans = np.zeros(shape=(4,1))
tomat.itemset(0,cornum)
tomat.itemset(1,sumx)
tomat.itemset(2,sumx2)
tomat.itemset(3,sumx3)
tomat.itemset(4,sumx)
tomat.itemset(5,sumx2)
tomat.itemset(6,sumx3)
tomat.itemset(7,sumx4)
tomat.itemset(8,sumx2)
tomat.itemset(9,sumx3)
tomat.itemset(10,sumx4)
tomat.itemset(11,sumx5)
tomat.itemset(12,sumx3)
tomat.itemset(13,sumx4)
tomat.itemset(14,sumx5)
tomat.itemset(15,sumx6)
toans.itemset(0,sumy)
toans.itemset(1,sumxy)
toans.itemset(2,sumx2y)
toans.itemset(3,sumx3y)
tosol = np.linalg.solve(tomat,toans)
y3 = tosol.item(0) + tosol.item(1)*x1 + tosol.item(2)*(x1**2) + tosol.item(3)*(x1**3)
plt.plot(x1,y3, color = "navy", linewidth="2", label="third order")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()

meanY = sumy/float(cornum)
Sr1 = Sr2 = Sr3 = St = 0.0
for i in range(0,cornum):
    Sr1 += ((ycor[i]-(fosol.item(0) + fosol.item(1)*xcor[i]))**2)
    Sr2 += ((ycor[i]-(sosol.item(0) + sosol.item(1)*xcor[i] + sosol.item(2)*(xcor[i]**2)))**2)
    Sr3 += ((ycor[i]-(tosol.item(0) + tosol.item(1)*xcor[i] + tosol.item(2)*(xcor[i]**2) + tosol.item(3)*(xcor[i]**3)))**2)
    St += ((ycor[i]-meanY)**2)
R1 = (St-Sr1)/St
R2 = (St-Sr2)/St
R3 = (St-Sr3)/St
print("First Order: y=("+str(fosol.item(0))+")"+"+("+str(fosol.item(1))+")"+"x")
print("Correlation Coefficient: ",R1,"\n")
print("Second Order: y=("+str(sosol.item(0))+")"+"+("+str(sosol.item(1))+")"+"x+("+str(sosol.item(2))+")"+"x^2")
print("Correlation Coefficient: ",R2,"\n")
print("Third Order: y=("+str(tosol.item(0))+")"+"+("+str(tosol.item(1))+")"+"x+("+str(tosol.item(2))+")"+"x^2+("+str(tosol.item(2))+")"+"x^3")
print("Correlation Coefficient: ",R3,"\n")



















   
