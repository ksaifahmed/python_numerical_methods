# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:55:14 2019

@author: home
"""

import numpy as np
import matplotlib.pyplot as p



def F(x):
    return (x/(1-x))*((6/(2+x))**0.5)-0.05



#GRAPHICAL MODEL:
    
x = np.arange(0.02822,0.02835,0.00000001)
y = F(x)
p.plot(x, y, color="navy")
y1 = x-x
p.plot(x, y1, color = "orange")
p.xlabel("x")
p.ylabel("function of Kp")
p.grid()
ridx = np.argwhere(np.diff(np.sign(y - y1))).flatten()
p.plot(x[ridx],F(x[ridx]),'ro')
p.savefig("Root Graph.pdf", dpi = 500)
print("The root by graphical method is: ", x[ridx])


#Exact value : 0.028249441148471142




def secant_meth(F, init_guess1, init_guess2, RAError, max_itr):
    itr = 0
    xr1 = init_guess1
    xR = init_guess2
    
    while True:
        if itr >= max_itr:
            break
        xr2 = xr1
        xr1 = xR
        xR = xr1 - (F(xr1)*(xr2-xr1))/(F(xr2)-F(xr1))
        itr += 1
        error = abs((xR - xr1)/xR)*100
#        print (error)
        if error <= RAError:
            break
    
    return "root: "+str(xR)+", iterations: "+str(itr)
        


def falsepos_meth(F, init_guess1, init_guess2, RAError, max_itr):
    itr = 0
    xu = init_guess1
    xl = init_guess2
    prev = 0.0
    
    stat1 = 0
    stat2 = 0
    
    
    if not F(xl)*F(xu) < 0 :
        return "Choose lower xl and upper xu guesses for the root such that: f(xl).f(xu)<0"
    
    while True:
        if itr >= max_itr:
            break
        xr = xu - (F(xu)*(xl-xu))/(F(xl)-F(xu))
        itr += 1
        
        if F(xr)*F(xl) == 0.0:
            return  "root: "+str(xr)+", iterations: "+str(itr)
        elif F(xr)*F(xl) < 0:
            xu = xr
            stat1 += 1
        elif F(xr)*F(xl) > 0:
            xl = xr
            stat2 += 1
            
        #modified false position   
        if stat1 == 2:
            xl /= 2.0
            stat2 = 0
        elif stat2 ==2:
            xu /= 2.0
            stat2 = 0
    
        error = abs((xr-prev)/xr)*100
        prev = xr
#        print(error)
        if error <= RAError:
            break
        
    return "root: "+str(xr)+", iterations: "+str(itr)
        
        
        
#print(secant_meth(F, 0, 3, 0.000000000001, 1000))        
#print(falsepos_meth(F, 0, 0.9, 0.00000000000001, 100))
        
        
        
        
        
        
        
        
        
        
        
    



















