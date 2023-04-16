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
        self.pixmap=None
        self.mixoutput=0
        self.imaginary = None
        self.magnitude = None
        self.phase = None
        self.unitphase=None
        self.unitmagnitude=None
        
   
    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode: 'Modes') -> np.ndarray:
       
        
        self.unitmagnitude=np.divide(imageToBeMixed.magnitude,imageToBeMixed.magnitude)
        self.unitphase=np.multiply(imageToBeMixed.phase,0)
    
        if (mode==Modes.magnitudeAndPhase):
            
            MagnitudeTemp = (magnitudeOrRealRatio/100)*imageToBeMixed.magnitude + ((100 - magnitudeOrRealRatio)/100)*self.magnitude
            PhaseTemp = (phaesOrImaginaryRatio/100)*imageToBeMixed.phase + ((100 - phaesOrImaginaryRatio)/100)*self.phase
            OutputTemp = MagnitudeTemp*np.cos(PhaseTemp)+ 1j*MagnitudeTemp*np.sin(PhaseTemp)
            inverseoutput = np.fft.ifft2(OutputTemp)
            return inverseoutput
        if (mode==Modes.realAndImaginary):
            realTmp = (magnitudeOrRealRatio/100)*imageToBeMixed.real + ((100 - magnitudeOrRealRatio)/100)*self.real
            iMagnitudeTemp = (phaesOrImaginaryRatio/100)*imageToBeMixed.imaginary + ((100 - phaesOrImaginaryRatio)/100)*self.imaginary
            OutputTemp =realTmp+ 1j*iMagnitudeTemp
            inverseoutput= np.fft.ifft2(OutputTemp)
            return inverseoutput
        if (mode==Modes.uniformMagnitudeandPhase):
            OutputTemp = self.unitmagnitude*np.cos(self.unitphase)+ 1j*self.unitmagnitude*np.sin(self.unitphase)
            inverseoutput = np.fft.ifft2(OutputTemp)
            return inverseoutput
        if (mode==Modes.uniformMagnitude):
            PhaseTemp = (phaesOrImaginaryRatio/100)*imageToBeMixed.phase + ((100 - phaesOrImaginaryRatio)/100)*self.phase
            OutputTemp = self.unitmagnitude*np.cos(PhaseTemp)+ 1j*self.unitmagnitude*np.sin(PhaseTemp)
            inverseoutput = np.fft.ifft2(OutputTemp)
            return inverseoutput
        if (mode==Modes.uniformPhase):
            MagnitudeTemp = (magnitudeOrRealRatio/100)*imageToBeMixed.magnitude + ((100 - magnitudeOrRealRatio)/100)*self.magnitude
            OutputTemp = MagnitudeTemp*np.cos(self.unitphase)+ 1j*MagnitudeTemp*np.sin(self.unitphase)
            inverseoutput = np.fft.ifft2(OutputTemp)
            return inverseoutput

    def Fourier(self):
         self.dft = np.fft.fft2(self.imgPath)

    def setImage(self,x):
            yourQImage=qimage2ndarray.array2qimage(x)
            pixmap = QPixmap(QPixmap.fromImage(yourQImage))
            self.pixmap=pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        

    def MagnitudeFT(self,n):
            self.Fourier()
            self.magnitude = np.abs(self.dft)
            self.setImage(self.magnitude)
            n.setPixmap((self.pixmap))
            print(self.magnitude)
        

    def PhaseFT(self,n):
            self.Fourier()
            self.phase = np.angle(self.dft)
            self.setImage(self.phase)
            n.setPixmap((self.pixmap))
            print(self.phase)

    def ImaginaryFT(self,n):
            self.Fourier()
            self.imaginary= np.imag(self.dft)
            self.setImage(self.imaginary)
            n.setPixmap((self.pixmap))
            print(self.imaginary)
    def RealFT(self,n):
            self.Fourier()
            self.real = np.real(self.dft)
            self.setImage(self.real)
            n.setPixmap((self.pixmap))
            print (self.real)

   
    

            
  

    
    


