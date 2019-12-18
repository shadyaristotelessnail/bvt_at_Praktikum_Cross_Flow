# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:12:04 2019

@author: Ibm
"""

import numpy as np
import matplotlib.pyplot as plt

A=0.1
leitf=np.array([69,9.3])
NaCl_konz= leitf/1.4841

#t=np.array([])




#Rückhaltevermögen
RG=np.array([NaCl_konz[1]/NaCl_konz[0]])
V_puffer=np.array([2.4])
V_F = np.array([0.8])

Rj=np.log(RG)*(V_F/V_puffer)+1
print("R für NaCl",Rj)

leitf2=np.array([69,56.7,48.5,42.3,35.3,29.4,24.7,20.9,17.5,14.6,12.4,10.8,9.3])
NaCl2=leitf2/1.4841
t=np.array([0,3.018,5.5717,9.0192,12.0313,15.1185,18.2136,21.3894,24.4836,28.1042,31.3675,35.136,38.5322])




def nacl_konz():
    plt.plot(t,NaCl2,'+k')
    plt.ylabel("NaCl-konzentration in g/l")
    plt.xlabel("Zeit in min")
    plt.title("NaCl-konzentration gegen die Zeit in min")
    plt.show()
nacl_konz()    

# Permeatfluss
def jp_plot():
    V=np.arange(0,2500,200)
    V_t=V/t
    print(V_t)
    Jp=V_t/A
    plt.plot(t,Jp,'*k')
    plt.title("Permeatfluss gegen die Zeit in min")
    plt.xlabel("t in min")
    plt.ylabel("Permeatfluss")
    plt.ylim(0,800)
    plt.show()
    
jp_plot()    

def pd_plot():
    pr=np.array([3.0,3.5,3.75,3.75,3.75,3.75,3.8,3.8,3.9,3.9,3.9,3.9,3.9])
    pf=np.array([6.0,6.3,6.3,6.3,6.3,6.3,6.5,6.5,6.5,6.5,6.5,6.5,6.5])
    dp=(pf+pr)/2
    plt.plot(t,dp,'*k')
    plt.xlabel("t in min")
    plt.ylim(0,6)
    plt.title("Transmembrane Druckdifferenz \u0394P gegen die Zeit in min")
    plt.ylabel("Transmembrane Druckdifferenz \u0394P")
    plt.show()
pd_plot()    