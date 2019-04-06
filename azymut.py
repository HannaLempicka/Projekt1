# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:51:30 2019

@author: hania
"""
from math import atan, degrees
import matplotlib.pyplot as plt  
    
def dms(Deg):
    d=int(Deg) #stopnie
    m=int((Deg-d)*60.0) #minuty
    s=(Deg-d-m/60.0)*3600.0 #sekundy
    s=round(s,5)
    
    if s==60:
        s=0
        m=m+1

    if m==60:
        m=0
        d=d+1
    return (d, m, s) #wynik końcowy


def az(Xa, Ya, Xb, Yb):
    if Xb-Xa == 0 and Yb-Ya > 0:
        az=90
    elif Xb-Xa == 0 and Yb-Ya < 0:
        az=270
    elif Xb-Xa != 0:
        az=degrees(atan((Yb-Ya)/(Xb-Xa)))
        if Xb-Xa>0 and Yb-Ya>0:
            az=az
        elif Xb-Xa>0 and Yb-Ya<0:
            az=az+180
        elif Xb-Xa<0 and Yb-Ya<0:
            az=az+180
        elif Xb-Xa<0 and Yb-Ya>0:
            az=az+360
    
    azdms =dms(az)
    return azdms
