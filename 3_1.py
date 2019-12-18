# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import quantities as pq
import matplotlib.pyplot as plt
import numpy as np

A=0.1

#
pr=np.array([1,1.5,2,2.5,3])
pF=np.array([3.5,4.0,4.5,5.0,5.4])
t=np.array([103.14,80.80,66.89,56.40,50.15])

tpd=(pr+pF)/2
print(tpd)

t=t/3600
Jp=(0.05/t)/A

Anstieg,Achsenabschnitt = np.polyfit(tpd,Jp,1)

print("Anstieg",Anstieg)
print("Achsenabschnitt",Achsenabschnitt)

x=np.linspace(2.25,4.5,100)
y=Anstieg*x+Achsenabschnitt

plt.plot(tpd,Jp,"*k")
plt.xlabel("Transmembrane Druckdifferenz \u0394P")
plt.ylabel("Permeatfluss Jp")
plt.xlim(tpd.min(),tpd.max())
plt.text(2.5,35,"y=9.49*x-3.88")
plt.plot(x,y)