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

##współrzędne a
#Xa=wczytaj(' Xa: ')
#Ya=wczytaj(' Ya: ')
##Współrzędne b
#Xb=wczytaj(' Xb: ')
#Yb=wczytaj(' Yb: ')
##Współrzędne c
#Xc=wczytaj(' Xc: ')
#Yc=wczytaj(' Yc: ')
#Yd=wczytaj(' Yd: ')
##Współrzędne d
#Xd=wczytaj(' Xd: ')

#%%
def pktprze(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd):
    import matplotlib.pyplot as plt    
    
    if ((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc)) != 0:
        t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
        
        Xp1=Xa+t1*(Xb-Xa) 
        Yp1=Ya+t1*(Yb-Ya)
        
        Xp=round(Xp1,3)
        Yp=round(Yp1,3)
        
        if t1>=0 and t1<=1 and t2>=0 and t2<=1:
            odp='punkt lezy na przecieciu odcinkow'
        elif t1>=0 and t1<=1 and t2<0 or t2>1:
            odp='punkt lezy na odcinku AB'
            plt.plot([Yc,Yp],[Xc,Xp],':')
        elif t2>=0 and t2<=1 and t1<0 or t1>1:
            odp='punkt lezy na odcinku CD'
            plt.plot([Ya,Yp],[Xa,Xp],':')
        else:
            odp='punkt lezy na przedluzeniu obu prostych'
            plt.plot([Ya,Yp],[Xa,Xp],':')
            plt.plot([Yc,Yp],[Xc,Xp],':')
        with open('wspP.txt', 'w') as plik:
            plik.write('{:^20s}|{:^20s}|{:s}\n'.format('Xp','Yp','polozenie punktu'))
            plik.write('{:^20.3f}|{:^20.3f}|{:s}'.format(Xp,Yp,odp))
        
        plt.plot([Ya,Yb],[Xa,Xb], label= 'Odc AB')
        plt.plot([Yc,Yd],[Xc,Xd], label= 'Odc CD')
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
    
    
    return(t1, t2, Xp, Yp)

#t1, t2, Xp, Yp, odp = pktprze(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd)
#print('Współrzędna Xp= ', Xp,'m')
#print('Współrzędna Yp= ', Xp,'m')
#print(odp)