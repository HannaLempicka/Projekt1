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
Yd  = 17957.410
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
    import matplotlib.pyplot as plt
    Xab=[]
    Yab=[]
    Xcd=[]
    Ycd=[]
    
    Xap=[]
    Yap=[]
    Xcp=[]
    Ycp=[]
    
    
    
    if ((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc)) != 0:
        t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        
        Xp1=Xa+t1*(Xb-Xa) 
        Yp1=Ya+t1*(Yb-Ya)
        
        Xp=round(Xp1,3)
        Yp=round(Yp1,3)
        
        Xap.append(Xa)
        Xap.append(Xp)
        Yap.append(Ya)
        Yap.append(Yp)
        Xcp.append(Xc)
        Xcp.append(Xp)
        Ycp.append(Yc)
        Ycp.append(Yp)
        
        if t1>=0 and t1<=1 and t2>=0 and t2<=1:
            odp='punkt lezy na przecieciu odcinkow'
        elif t1>=0 and t1<=1 and t2<=0 or t2>=1:
            odp='punkt lezy na odcinku AB'
            plt.plot(Ycp,Xcp,':')
        elif t1<=0 or t1>=1 and t2>=0 and t2<=1:
            odp='punkt lezy na odcinku CD'
            plt.plot(Yap,Xap,':')
        else:
            odp='punkt lezy na przedłuezniu obu prostych'
        with open('wspP.txt', 'w') as plik:
            plik.write('{:^20s}|{:^20s}|{:s}\n'.format('Xp','Yp','polozenie punktu'))
            plik.write('{:^20.3f}|{:^20.3f}|{:s}'.format(Xp,Yp,odp))
        
        Xab.append(Xa)
        Xab.append(Xb)
        Yab.append(Ya)
        Yab.append(Yb)
        
        Xcd.append(Xc)
        Xcd.append(Xd)
        Ycd.append(Yc)
        Ycd.append(Yd)
        
        plt.plot(Yab,Xab, label= 'Odc AB')
        plt.plot(Ycd,Xcd, label= 'Odc CD')
        plt.scatter(Yp,Xp, label= 'pkt P')
        plt.scatter(Ya,Xa, label= 'pkt A')
        plt.scatter(Yb,Xb, label= 'pkt B')
        plt.scatter(Yc,Xc, label= 'pkt C')
        plt.scatter(Yd,Xd, label= 'pkt D')
        plt.legend()
        
    else:
        odp='punkt przecięcia nie istnieje bo proste są rownolegle'
        Xp='brak'
        Yp='brak'
    
    
    return(Xp, Yp, odp)

Xp, Yp, odp = pktprze(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd)
print(Xp, Yp, odp)