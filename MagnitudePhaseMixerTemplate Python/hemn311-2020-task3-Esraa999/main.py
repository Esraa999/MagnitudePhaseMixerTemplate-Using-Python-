import sys
import numpy as np
from scipy import fftpack 
import qimage2ndarray
import cv2
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from imageModel import ImageModel
from gui import Ui_MainWindow




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.imageob=ImageModel(self)
        
    
        self.image = None
        self.imgp=None
        self.imgPath=None
        self.imagegrey=None
        
        self.ui.comboBox.activated[str].connect(self.combochanger1)
        self.ui.comboBox_2.activated[str].connect(self.combochanger2)
        
        self.ui.horizontalSlider.valueChanged.connect(self.changeValue1)
        self.ui.horizontalSlider_2.valueChanged.connect(self.changeValue2)
     
        


        self.ui.BrowseButton.clicked.connect(lambda: self.browse(self.ui.Imagelbl))
        self.ui.BrowseButton_2.clicked.connect(lambda: self.browse(self.ui.Imagelbl_3))

    def browse(self,m):
    
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file','',"Image files (*.jpg *.png *jpeg)")
        
        
    
        self.imgreading=cv2.imread(filename, cv2.COLOR_BGR2GRAY)
        self.imageob.imgPath=self.imgreading
        pixmap = QtGui.QPixmap(filename)
        pic=pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        m.setPixmap(pic)
    
       
       
       


    def changeValue1(self,value): 
      
        scaledValue = float(value)/10
        self.v1=scaledValue
        print ("v1=",self.v1)

    def changeValue2(self,value): 
      
        scaledValue = float(value)/10
        self.v1=scaledValue
        print ("v2=",self.v1)
        
 
        
 
            

    def combochanger1(self):
        if self.ui.comboBox.currentText()=="Magnitude":
            print("1")
            self.imageob.MagnitudeCombo(self.ui.Imagelbl_2)
        elif self.ui.comboBox.currentText()=="Phase":
            print("2")
            self.imageob.PhaseCombo(self.ui.Imagelbl_2)
        elif self.ui.comboBox.currentText()=="Imaginary":
            print("3")
            self.imageob.ImaginaryCombo(self.ui.Imagelbl_2)
        elif self.ui.comboBox.currentText()=="Real":
            print("4")
            self.imageob.RealCombo(self.ui.Imagelbl_2)
    def combochanger2(self):
        if self.ui.comboBox_2.currentText()=="Magnitude":
            print("1")
            self.imageob.MagnitudeCombo(self.ui.Imagelbl_4)
        elif self.ui.comboBox_2.currentText()=="Phase":
            print("2")
            self.imageob.PhaseCombo(self.ui.Imagelbl_4)
        elif self.ui.comboBox_2.currentText()=="Imaginary":
            print("3")
            self.imageob.ImaginaryCombo(self.ui.Imagelbl_4)
        elif self.ui.comboBox_2.currentText()=="Real":
            print("4")
            self.imageob.RealCombo(self.ui.Imagelbl_4)
    

    

        

       


    
  
   
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
    


if __name__ == "__main__":
    main()
    
    