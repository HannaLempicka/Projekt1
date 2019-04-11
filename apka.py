# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:34:41 2019

@author: hania
"""
import sys

from PunktPrzeciecia import pktprze
from azymut import az, dms

from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QApplication, QGridLayout, QColorDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class AppWindow(QWidget):
    def __init__ (self):
        super().__init__()
        self.title="matplotlib przyklad"
        self.initInterface()
        self.initWidget()
        
    def initInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1200, 800) #pierwsze 2 to gdzie jest apka a następne to wymiary
        self.show()
    
    def initWidget(self):
        btn= QPushButton('Rysuj + wsp P', self)
        btnColAB= QPushButton('Kolor AB', self)
        btnColCD= QPushButton('Kolor CD', self)
        btnCzysc= QPushButton('Czysc', self)
        xaLabel = QLabel('{:^}'.format('Xa'), self)
        yaLabel = QLabel('Ya', self)
        xbLabel = QLabel('Xb', self)
        ybLabel = QLabel('Yb', self)
        xcLabel = QLabel('Xc', self)
        ycLabel = QLabel('Yc', self)
        xdLabel = QLabel('Xd', self)
        ydLabel = QLabel('Yd', self)
        xpLabel = QLabel('Xp', self)
        ypLabel = QLabel('Yp', self)
        odpLabel = QLabel('{:>50s}'.format('odpowiedź'), self)
        azABLabel = QLabel('{:>50s}'.format('azymut AB'), self)
        azCDLabel = QLabel('{:>50s}'.format('azymut CD'), self)
        azBALabel = QLabel('{:>50s}'.format('azymut BA'), self)
        azDCLabel = QLabel('{:>50s}'.format('azymut DC'), self)
        azABopLabel = QLabel('{:<30s}'.format('(stopnie, minuty, sekundy)'), self)
        azCDopLabel = QLabel('{:<30s}'.format('(stopnie, minuty, sekundy)'), self)
        azBAopLabel = QLabel('{:<30s}'.format('(stopnie, minuty, sekundy)'), self)
        azDCopLabel = QLabel('{:<30s}'.format('(stopnie, minuty, sekundy)'), self)
        self.xaEdit = QLineEdit()
        self.yaEdit = QLineEdit()
        self.xbEdit = QLineEdit()
        self.ybEdit = QLineEdit()
        self.xcEdit = QLineEdit()
        self.ycEdit = QLineEdit()
        self.xdEdit = QLineEdit()
        self.ydEdit = QLineEdit()
        self.xpEdit = QLineEdit()
        self.ypEdit = QLineEdit()
        self.odpEdit = QLineEdit()
        self.azABEdit = QLineEdit()
        self.azCDEdit = QLineEdit()
        self.azBAEdit = QLineEdit()
        self.azDCEdit = QLineEdit()
        
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        #wyswietlenie
        grid  = QGridLayout()
        grid.addWidget(xaLabel, 0, 0)
        grid.addWidget(self.xaEdit, 0, 1)
        
        grid.addWidget(yaLabel, 1, 0)
        grid.addWidget(self.yaEdit, 1, 1)
        
        grid.addWidget(xbLabel, 0, 2)
        grid.addWidget(self.xbEdit, 0, 3)
        
        grid.addWidget(ybLabel, 1, 2)
        grid.addWidget(self.ybEdit, 1, 3)
        
        grid.addWidget(xcLabel, 0, 4)
        grid.addWidget(self.xcEdit, 0, 5)
#        
        grid.addWidget(ycLabel, 1, 4)
        grid.addWidget(self.ycEdit, 1, 5)
#        
        grid.addWidget(xdLabel, 0, 6)
        grid.addWidget(self.xdEdit, 0, 7)
        
        grid.addWidget(ydLabel, 1, 6)
        grid.addWidget(self.ydEdit, 1, 7)
        
        grid.addWidget(btn, 3, 2, 1, 2)
        grid.addWidget(btnColAB, 3, 4, 1, 2)
        grid.addWidget(btnColCD, 3, 6, 1, 2)
        
        grid.addWidget(btnCzysc, 5, 6, 1, 2)
        
        
        grid.addWidget(ypLabel, 4, 2)
        grid.addWidget(self.ypEdit, 4, 3)
        
        grid.addWidget(xpLabel, 4, 4)
        grid.addWidget(self.xpEdit, 4, 5)
        
        grid.addWidget(odpLabel, 5, 1, 1, 2)
        grid.addWidget(self.odpEdit, 5, 3, 1, 3)
        
        grid.addWidget(azABLabel, 6, 1, 1, 2)
        grid.addWidget(self.azABEdit, 6, 3, 1, 2)
        
        grid.addWidget(azCDLabel, 7, 1, 1, 2)
        grid.addWidget(self.azCDEdit, 7, 3, 1, 2)
        
        grid.addWidget(azBALabel, 8, 1, 1, 2)
        grid.addWidget(self.azBAEdit, 8, 3, 1, 2)
        
        grid.addWidget(azDCLabel, 9, 1, 1, 2)
        grid.addWidget(self.azDCEdit, 9, 3, 1, 2)
        
        grid.addWidget(azABopLabel, 6, 5)
        grid.addWidget(azCDopLabel, 7, 5)
        
        grid.addWidget(azBAopLabel, 8, 5)
        grid.addWidget(azDCopLabel, 9, 5)
        
        grid.addWidget(self.canvas, 10, 1, 10, -1)
              
        self.setLayout(grid)
        
        btn.clicked.connect(self.oblicz)
        btnColAB.clicked.connect(self.zmienKolor)
        btnColCD.clicked.connect(self.zmienKolor2)
        btnCzysc.clicked.connect(self.czysc)
    
    def czysc(self):
        self.xaEdit.clear()
        self.yaEdit.clear()
        self.xbEdit.clear()
        self.ybEdit.clear()
        self.xcEdit.clear()
        self.ycEdit.clear()
        self.xdEdit.clear()
        self.ydEdit.clear()
        self.xpEdit.clear()
        self.ypEdit.clear()
        self.odpEdit.clear()
        self.azABEdit.clear()
        self.azCDEdit.clear()
        
    
    def zmienKolor(self):
        kolor = QColorDialog.getColor()
        if kolor.isValid():
#            print(kolor.name())
            self.rysuj(kol=kolor.name())
    
    def zmienKolor2(self):
        kolor = QColorDialog.getColor()
        if kolor.isValid():
#            print(kolor.name())
            self.rysuj(kol2=kolor.name())
        
     
    def SprawdzLiczbe(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus() #wstawianie kursora tam gdzie jest błąd
            return None #zwracamy nic
    
    def oblicz(self): #definicja przycisku musi mieć stylko self, a w rysuj jest jeszcze kol, więc tak to się obchodzi
        self.rysuj()
        
        
    def rysuj(self, kol='red', kol2='blue'):
        xa = self.SprawdzLiczbe(self.xaEdit)
        ya = self.SprawdzLiczbe(self.yaEdit)
        xb = self.SprawdzLiczbe(self.xbEdit)
        yb = self.SprawdzLiczbe(self.ybEdit)
        xc = self.SprawdzLiczbe(self.xcEdit)
        yc = self.SprawdzLiczbe(self.ycEdit)
        xd = self.SprawdzLiczbe(self.xdEdit)
        yd = self.SprawdzLiczbe(self.ydEdit)
#        print(xa,ya)
#        print(xb,yb)
#        print(xc,yc)
#        print(xd,yd)
        
        if None not in [xa,ya,xb,yb,xc,yc,xd,yd]:
            xa = float(self.xaEdit.text())
            ya = float(self.yaEdit.text())
            xb = float(self.xbEdit.text())
            yb = float(self.ybEdit.text())
            xc = float(self.xcEdit.text())
            yc = float(self.ycEdit.text())
            xd = float(self.xdEdit.text())
            yd = float(self.ydEdit.text())
            
            t1, t2, xp, yp, odp=pktprze(xa,ya,xb,yb,xc,yc,xd,yd)
            azAB=az(xa, ya, xb, yb)
            azCD=az(xc, yc, xd, yd)
            
            self.xpEdit.setText(str(xp))
            self.ypEdit.setText(str(yp))
            self.odpEdit.setText(odp)
            

            if None not in [t1, t2]:
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                if t1>=0 and t1<=1:
                    if t2>=0 and t2<=1:
                        pass
                    else:
                        ax.plot([yc,yp],[xc,xp],':')
                else:
                    if t2>=0 and t2<=1:
                        ax.plot([ya,yp],[xa,xp],':')
                    else:
                        ax.plot([yc,yp],[xc,xp],':')
                        ax.plot([ya,yp],[xa,xp],':')
                        
                ax.plot([ya, yb], [xa, xb], color=kol, label= 'Odc AB')
                ax.plot([yc, yd], [xc, xd], color=kol2, label= 'Odc CD')
                ax.scatter(yp,xp, label= 'pkt P')
                ax.scatter(ya,xa, label= 'pkt A')
                ax.scatter(yb,xb, label= 'pkt B')
                ax.scatter(yc,xc, label= 'pkt C')
                ax.scatter(yd,xd, label= 'pkt D')
                
                if azAB <= 180:
                    self.azABEdit.setText(str(dms(azAB)))
                    if xb-xa == 0 and yb-ya > 0:
#                        print(1)
                        ax.plot([ya, ya], [xa, xa+abs(ya-yb)/2], ':', label= 'N')    
                        ax.annotate('',
                                xy=(ya, xa+abs(ya-yb)/6), xycoords='data',
                                xytext=(ya+abs(ya-yb)/6, xa), textcoords='data',
                                arrowprops=dict(arrowstyle="<-",
                                                connectionstyle="arc3,rad=.4"))
                    elif yb==ya and xb>xa:
                        pass
                    
                    elif yb==ya:
#                        print(2)
                        ax.plot([yb, yb], [xa, xa+abs(xa-xb)/2], ':', label= 'N')
                        ax.annotate('',
                                    xy=(ya, xa+abs(xa-xb)/4), xycoords='data',
                                    xytext=(ya, xa-abs(xb-xa)/4), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                    else:
#                        print(3)
                        ax.plot([ya, ya], [xa, xa+abs(xa-xb)/2], ':', label= 'N')
                        a=(xb-xa)/(yb-ya)
                        b=xa-a*ya
                        ax.annotate('',
                                    xy=(ya, xa+abs(xa-xb)/4), xycoords='data',
                                    xytext=(ya+abs(ya-yb)/6, a*(ya+abs(ya-yb)/6)+b), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                
                elif azAB > 180:
                    self.azBAEdit.setText(str(dms(azAB)))
                    if xa-xb == 0 and ya-yb > 0:
#                        print(4)
                        ax.plot([yb, yb], [xb, xb+abs(yb-ya)/2], ':', label='N')    
                        ax.annotate('',
                                xy=(yb, xb+abs(yb-ya)/6), xycoords='data',
                                xytext=(yb+abs(yb-ya)/6, xb), textcoords='data',
                                arrowprops=dict(arrowstyle="<-",
                                                connectionstyle="arc3,rad=.4"))
                    
                    elif ya==yb:
#                        print(5)
                        ax.plot([ya, ya], [xb, xb+abs(xb-xa)/2], ':', label='N')
                        ax.annotate('',
                                    xy=(yb, xb+abs(xb-xa)/4), xycoords='data',
                                    xytext=(yb, xa-abs(xa-xb)/4), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                    else:
#                        print(6)
                        ax.plot([yb, yb], [xb, xb+abs(xb-xa)/2], ':', label='N')
                        a=(xa-xb)/(ya-yb)
                        b=xb-a*yb
                        ax.annotate('',
                                    xy=(yb, xb+abs(xb-xa)/4), xycoords='data',
                                    xytext=(yb+abs(yb-ya)/6, a*(yb+abs(yb-ya)/6)+b), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                if azCD <= 180:
                    self.azCDEdit.setText(str(dms(azCD)))
                    if xd-xc == 0 and yd-yc > 0:
#                        print(7)
                        ax.plot([yc, yc], [xc, xc+abs(yc-yd)/2], ':', label='N')    
                        ax.annotate('',
                                xy=(yc, xc+abs(yc-yd)/6), xycoords='data',
                                xytext=(yc+abs(yc-yd)/6, xc), textcoords='data',
                                arrowprops=dict(arrowstyle="<-",
                                                connectionstyle="arc3,rad=.4"))
                    elif yd==yc and xd>xc:
                        pass
                    
                    elif yd==yc:
#                        print(8)
                        ax.plot([yd, yd], [xc, xc+abs(xc-xd)/2], ':', label='N')
                        ax.annotate('',
                                    xy=(yc, xc+abs(xc-xd)/4), xycoords='data',
                                    xytext=(yd, xc-abs(xd-xc)/4), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                    else:
#                        print(9)
                        ax.plot([yc, yc], [xc, xc+abs(xc-xd)/2], ':', label='N')
                        a=(xd-xc)/(yd-yc)
                        b=xc-a*yc
                        ax.annotate('',
                                    xy=(yc, xc+abs(xc-xd)/4), xycoords='data',
                                    xytext=(yc+abs(yc-yd)/6, a*(yc+abs(yc-yd)/6)+b), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                
                elif azCD > 180:
                    self.azDCEdit.setText(str(dms(azCD)))
                    if xc-xd == 0 and yc-yd > 0:
#                        print(10)
                        ax.plot([yd, yd], [xd, xd+abs(yd-yc)/2], ':', label='N')    
                        ax.annotate('',
                                xy=(yd, xd+abs(yd-yc)/6), xycoords='data',
                                xytext=(yd+abs(yd-yc)/6, xd), textcoords='data',
                                arrowprops=dict(arrowstyle="<-",
                                                connectionstyle="arc3,rad=.4"))
                    elif yc==yd:
#                        print(11)
                        ax.plot([yc, yc], [xd, xd+abs(xd-xc)/2], ':', label='N')
                        ax.annotate('',
                                    xy=(yd, xd+abs(xd-xc)/4), xycoords='data',
                                    xytext=(yd, xc-abs(xc-xd)/4), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))
                    else:
#                        print(12)
                        ax.plot([yd, yd], [xd, xd+abs(xd-xc)/2], ':', label='N')
                        a=(xc-xd)/(yc-yd)
                        b=xd-a*yd
                        ax.annotate('',
                                    xy=(yd, xd+abs(xd-xc)/4), xycoords='data',
                                    xytext=(yd+abs(yd-yc)/6, a*(yd+abs(yc-yd)/6)+b), textcoords='data',
                                    arrowprops=dict(arrowstyle="<-",
                                                    connectionstyle="arc3,rad=0.4"))          
                ax.legend()
                self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

    
    
    