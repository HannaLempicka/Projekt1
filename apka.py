# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:34:41 2019

@author: hania
"""
import sys

from PunktPrzeciecia import pktprze
from azymut import az

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
        btnCol= QPushButton('Kolor', self)
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
        azABopLabel = QLabel('{:<50s}'.format('(stopnie, minuty, sekundy)'), self)
        azCDopLabel = QLabel('{:<50s}'.format('(stopnie, minuty, sekundy)'), self)
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
        grid.addWidget(btnCol, 3, 5, 1, 2)
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
        
        grid.addWidget(azABopLabel, 6, 5)
        grid.addWidget(azCDopLabel, 7, 5)
        
        grid.addWidget(self.canvas, 8, 1, 10, -1)
              
        self.setLayout(grid)
        
        btn.clicked.connect(self.oblicz)
        btnCol.clicked.connect(self.zmienKolor)
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
     
    def SprawdzLiczbe(self, element):
        if element.text().lstrip('-').replace('.','',1).isdigit():
            return float(element.text())
        else:
            element.setFocus() #wstawianie kursora tam gdzie jest błąd
            return None #zwracamy nic
    
    def oblicz(self): #definicja przycisku musi mieć stylko self, a w rysuj jest jeszcze kol, więc tak to się obchodzi
        self.rysuj()
        
        
    def rysuj(self, kol='red'):
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
            self.azABEdit.setText(str(azAB))
            self.azCDEdit.setText(str(azCD))

            if None not in [t1, t2]:
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                if t1>=0 and t1<=1 and t2<0 or t2>1:
                    ax.plot([yc,yp],[xc,xp],':')
                elif t2>=0 and t2<=1 and t1<0 or t1>1:
                    ax.plot([ya,yp],[xa,xp],':')
                else:
                    ax.plot([yc,yp],[xc,xp],':')
                    ax.plot([ya,yp],[xa,xp],':')
                ax.plot([ya, yb], [xa, xb], color=kol, label= 'Odc AB')
                ax.plot([yc, yd], [xc, xd], color=kol, label= 'Odc CD')
                ax.scatter(yp, xp, label= 'pkt P')
                ax.scatter(ya,xa, label= 'pkt A')
                ax.scatter(yb,xb, label= 'pkt B')
                ax.scatter(yc,xc, label= 'pkt C')
                ax.scatter(yd,xd, label= 'pkt D')
                ax.legend()
                self.canvas.draw()
    
    def wpisz(self):
        self.xEdit.setText('1')

def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

    
    
    