# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:22:59 2019

@author: hania
"""
#Wyznaczenie przecięcia dwóch odcinków

#Przykładowe dane
#Xa  = 1186.000
#Ya  = 17962.690
#Xb  = 1144.740
#Yb  = 18006.220
#Xc  = 1184.310
#Yc  = 18004.140
#Xd  = 1151.140
#Yd  = 17957.410
#Xp  = 1168.210
#Yp  = 17981.459

#%%
def wczytaj(wsp):
    #współrzędna to ciąg znaków np'Xa'
    komunikat='Podaj'+wsp
    x=input(komunikat)
    while x.lstrip('-').replace('.','',1).isdigit() == 0:
        x=input('To nie jest współrzędna. ' + komunikat)
    return(float(x))

#współrzędne a
Xa=wczytaj(' Xa: ')
Ya=wczytaj(' Ya: ')
#Współrzędne b
Xb=wczytaj(' Xb: ')
Yb=wczytaj(' Yb: ')
#Współrzędne c
Xc=wczytaj(' Xc: ')
Yc=wczytaj(' Yc: ')
#Współrzędne d
Xd=wczytaj(' Xd: ')
Yd=wczytaj(' Yd: ')

#%%

def pktprze(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd):
    
    if ((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc)) != 0:
        t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        
        Xp1=Xa+t1*(Xb-Xa) 
        Yp1=Ya+t1*(Yb-Ya)
        
        Xp=round(Xp1,3)
        Yp=round(Yp1,3)
        
        if t1>0 and t1<1 and t2>0 and t2<1:
            odp='punkt leży na przecięciu odcinków'
        elif t1>0 and t1<1 and t2<0 or t2>1:
            odp='punkt leży na odcinku AB'
        elif t1<0 or t1>1 and t2>0 and t2<1:
            odp='punkt leży na odcinku CD'
        else:
            odp='punkt leży na przedłużeniu obu prostych'
    
    else:
        odp='punkt przecięcia nie istnieje bo proste są równoległe'
        Xp='brak'
        Yp='brak'
        
    
    
    return(Xp, Yp, odp)

Xp, Yp, odp= pktprze(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd)

print(Xp, Yp, odp)