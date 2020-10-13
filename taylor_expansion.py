# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:05:55 2019

@author: home
"""

import numpy as np
import math as m

def taylorlog(x, itr):
    sum =  0.0
    for i in range(1,itr+1):
        sum += ((x**i)/(i))*((-1)**(i+1))
    return sum
vecfunc = np.vectorize(taylorlog)


def errorfunc(itr):
    return abs(vecfunc(0.5,itr)-vecfunc(0.5,itr-1))/vecfunc(0.5,itr)

import matplotlib.pyplot as p
x = np.arange(-1.0,1.1,0.1)
x = x[x > -1.0]
y = np.log(1+x)
p.grid()
p.figure(1)
p.xlabel("x")
p.ylabel("y = ln (1+x)")
p.plot(x,y,'bd-',color="red",linewidth = 2.0, label = "exact solution")
p.legend()


x = np.arange(-1.0,1.1,0.1)
x = x[x > -1.0]
y = taylorlog(x,1)
p.plot(x,y,'b.-',color="orange",linewidth = 2.0, label = "itrns: 1")
p.legend()

x = np.arange(-1.0,1.1,0.1)
x = x[x > -1.0]
y = taylorlog(x,3)
p.plot(x,y,'b.-',color="green",linewidth = 2.0, label = "itrns: 3")
p.legend()

x = np.arange(-1.0,1.1,0.1)
x = x[x > -1.0]
y = taylorlog(x,5)
p.plot(x,y,'b.-',color="yellow",linewidth = 2.0, label = "itrns: 5")
p.legend()

x = np.arange(-1.0,1.1,0.1)
x = x[x > -1.0]
y = taylorlog(x,20)
p.plot(x,y,'b.-',color="blue",linewidth = 2.0, label = "itrns: 20")
p.legend()

x = np.arange(-1.0,1.1,0.1)
x = x[x > -1.0]
y = taylorlog(x,50)
p.plot(x,y,'b.-',color="navy",linewidth = 2.0, label = "itrns: 50")
p.legend()

#graph saved
#p.savefig("First Graph.pdf", dpi = 500)

#second graph
p.figure(2)
iterations = np.arange(1,51,1)
error = errorfunc(iterations)*100
p.plot(iterations, error, '-', color="lightblue", label = "ln(1.5) using taylor expansion", linewidth = 2.0)
p.legend()
p.grid()
p.plot(iterations, error, 'd', color="navy")
p.xlabel("Number of Iterations")
p.ylabel("Relative Approximation Error in %")
#graph saved
p.savefig("Error Graph.pdf", dpi = 500)


i = 4
while i:
     print("Enter value of x: ")
     x = float(input())
     print("Enter number of iterations:")
     iterations = int(input())
     print("Value of ln("+str(1+x)+") for " ,iterations, "iterations is: ", taylorlog(x, iterations))
     i -= 1
    




