## This is the abstract class that the students should implement  

from modesEnum import Modes
import numpy as np
import sys
from scipy import fftpack 
import qimage2ndarray
import cv2
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os


class ImageModel():

    """
    A class that represents the ImageModel"
    """
    def __init__(self):
        pass
        
       
        

    def __init__(self, imgPath: str):
        self.imgPath = imgPath
    
        
        
        self.imgByte = None
        self.dft = None
        self.real = None

        self.imaginary = None
        self.magnitude = None
        self.phase = None

        
   
    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode: 'Modes') -> np.ndarray:
        """
        a function that takes ImageModel object mag ratio, phase ration 
        """
        ### 
        # implement this function
        ###
        pass

    
    
    def MagnitudeCombo(self,n):

            f = np.fft.fft2(self.imgPath)
            fshift = np.fft.fftshift(f)
            self.magnitude = np.abs(fshift)
            yourQImage=qimage2ndarray.array2qimage(self.magnitude)
            pixmap = QPixmap(QPixmap.fromImage(yourQImage))
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            n.setScaledContents(True)
            n.setPixmap((image))
            print(self.magnitude)
    def PhaseCombo(self,n):
        
            f = np.fft.fft2(self.imgPath)
            fshift = np.fft.fftshift(f)
            self.phase = np.angle(fshift)
            yourQImage=qimage2ndarray.array2qimage(self.phase)
            pixmap = QPixmap(QPixmap.fromImage(yourQImage))
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            n.setScaledContents(True)
            n.setPixmap((image))
            print(self.phase)
    def ImaginaryCombo(self,n):
        
            f = np.fft.fft2(self.imgPath)
            self.imaginary= np.imag(f)
            yourQImage=qimage2ndarray.array2qimage(self.imaginary)
            pixmap = QPixmap(QPixmap.fromImage(yourQImage))
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            n.setScaledContents(True)
            n.setPixmap((image))
            print(self.imaginary)
    def RealCombo(self,n):
        
            f = np.fft.fft2(self.imgPath)
            self.real = np.real(f)
            yourQImage=qimage2ndarray.array2qimage(self.real)
            pixmap = QPixmap(QPixmap.fromImage(yourQImage))
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            n.setScaledContents(True)
            print (self.real)
            n.setPixmap((image))
  

    
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow = QtWidgets.QMainWindow()
    img=ImageModel(self)
    MainWindow.show()
    imgg=ImageModel()
    imagg.show()
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())