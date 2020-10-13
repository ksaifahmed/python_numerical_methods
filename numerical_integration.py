# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:39:08 2019

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt

file = open("dataset.txt","r")
n = int(file.readline())
xar = []
fxar = []

lines = file.readlines()
for line in lines:
    x,fx = (line.split(" "))
    xar.append(float(x))
    fxar.append(float(fx))
    
file.close()
#print(xar, fxar)
plt.figure(figsize=(12,10))
plt.grid()
plt.scatter(xar,fxar, color ="navy",s=100)
plt.plot(xar,fxar,linewidth=2.0,color="green")
ti = s1 = s2 = 0

def Trap(a,b,fa,fb):
    global ti
    sm = 0.0
    sm = ((b-a)*(fa+fb))/2.0
    x = []
    x.extend([a,b])
    y = []
    y.extend([fa,fb])
    if ti == 0:
        plt.fill_between(x,y,color="cyan",label="Trapezoid")
        ti=1
    else:
        plt.fill_between(x,y,color="cyan")
    
    return sm

def Simp13(a,m,b,fa,fm,fb):
    global s1
    sm = 0.0
    sm = ((b-a)*(fa+4*fm+fb))/6.0
    x = []
    x.extend([a,m,b])
    y = []
    y.extend([fa,fm,fb])
    if s1 == 0:
        plt.fill_between(x,y,color="orange",label="Simpson's 1/3")
        s1 = 1
    else:
        plt.fill_between(x,y,color="orange")
    return sm

def Simp38(a,m1,m2,b,fa,fm1,fm2,fb):
    global s2
    sm = 0.0
    sm = ((b-a)*(fa+3*fm1+3*fm2+fb))/8.0
    x = []
    x.extend([a,m1,m2,b])
    y = []
    y.extend([fa,fm1,fm2,fb])
    if s2 == 0:
        plt.fill_between(x,y,color="yellow",label="Simpson's 3/8")
        s2 = 1
    else:
        plt.fill_between(x,y,color="yellow")
    return sm



def integrate(n,xar,fxar):
    intgr = 0.0
    i = 0
    tp = s13 = s38 = 0
    while i<n-1:
        k = 1
        dx = xar[i+1]-xar[i]
        j = i
        while j<n-2:
            j += 1
            dx1 = xar[j+1]-xar[j]
            if abs(dx-dx1)>=0.00001:
                break
            k+=1
        dx = dx1
        if(k==1):
            intgr += Trap(xar[i],xar[i+1],fxar[i],fxar[i+1])
            tp += 1
        elif(k==2):
            intgr += Simp13(xar[i],xar[i+1],xar[i+2],fxar[i],fxar[i+1],fxar[i+2])
            s13 += 2
        elif(k==3):
            intgr += Simp38(xar[i],xar[i+1],xar[i+2],xar[i+3],fxar[i],fxar[i+1],fxar[i+2],fxar[i+3])
            s38 += 3
        elif(k%3==0):
            m = i
            for j in range(0,k/3):
                intgr += Simp38(xar[m],xar[m+1],xar[m+2],xar[m+3],fxar[m],fxar[m+1],fxar[m+2],fxar[m+3])
                s38 += 3
                m += 3
        elif(k%3==2):
            m = i
            while m<k-4+i:
                intgr += Simp38(xar[m],xar[m+1],xar[m+2],xar[m+3],fxar[m],fxar[m+1],fxar[m+2],fxar[m+3])
                s38 += 3
                m += 3
            while m<k+i:
                intgr += Simp13(xar[m],xar[m+1],xar[m+2],fxar[m],fxar[m+1],fxar[m+2])
                s13 += 2
                m += 2
        elif(k%3==1):
            m = i
            while m<k-2+i:
                intgr += Simp38(xar[m],xar[m+1],xar[m+2],xar[m+3],fxar[m],fxar[m+1],fxar[m+2],fxar[m+3])
                s38 += 3
                m += 3
            intgr += Simp13(xar[m],xar[m+1],xar[m+2],fxar[m],fxar[m+1],fxar[m+2])
            s13 += 2
        i += (k)
        
    print("Trapezoid: "+str(tp)+" intervals")
    print("1/3 rule: "+str(s13)+" intervals")
    print("3/8 rule: "+str(s38)+" intervals")
    print("\nIntegral Value: "+str(round(intgr,5)))
    
    
def plotter(xar,fxar):
    i = 0
    x1 = np.arange(xar[0],xar[n-1],0.01)
    y1 = x1-x1
    plt.plot(x1,y1,linewidth=2.5,color="black")
    for fx in fxar:
        if fx >= 0.0:
            y1 = np.arange(0.0,fx,0.01)
            x1 = y1-y1+xar[i]
            plt.plot(x1,y1,color="crimson",linewidth=3,linestyle="--")
            i += 1
        else:
            y1 = np.arange(fx,0.0,0.01)
            x1 = y1-y1+xar[i]
            plt.plot(x1,y1,color="crimson",linewidth=3,linestyle="--")
            i += 1
    plt.legend()
    plt.show()
        
            









#print("",xar,"\n",fxar)
integrate(n,xar,fxar)       
plotter(xar,fxar)







