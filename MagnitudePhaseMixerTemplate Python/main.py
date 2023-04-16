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
from PIL import Image
from imageModel import ImageModel
from gui import Ui_MainWindow
from modesEnum import Modes
import logging




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sizeofimage=0
        self.imageob=ImageModel(self)
        self.MagorRealslidervalue=0.0
        self.PhaseorImaginartvalue=0.0
        self.magOrRealratio=0.0
        self.phaseOrImgratio=0.0
        self.Imageob=ImageModel(self)
        self.ImageObjectOne=ImageModel(self)
        self.ImageObjectTwo=ImageModel(self)
        self.imageNotmix=ImageModel(self)
        self.mode=Modes
        self.filename = None
        self.qimg=None
        self.mixout=None
        self.modeone=''
        self.modetwo=''
        self.imageToBeMixed=''
        self.height1=0
        self.height2=0
        self.width1=0
        self.width2=0
        self.ui.comboBox.activated[str].connect(lambda: self.combofftchanger(1))
        self.ui.comboBox_2.activated[str].connect(lambda: self.combofftchanger(2))
        self.ui.comboBox_5.activated[str].connect(lambda: self.ImageChanger(1))
        self.ui.comboBox_6.activated[str].connect(lambda: self.ImageChanger(2))
        self.ui.comboBox_7.activated[str].connect(lambda: self.ComboBoxes7and8(1))
        self.ui.comboBox_3.activated[str].connect(self.outputup)
        self.ui.comboBox_8.activated[str].connect(lambda: self.ComboBoxes7and8(2))
        self.ui.MagandPhaseSlider.valueChanged[int].connect(self.changeValue)
        self.ui.RealandImagSlider.valueChanged[int].connect(self.changeValue)
        self.ui.BrowseButton.clicked.connect(lambda: self.browse(self.ImageObjectOne,self.ui.Imagelbl,1))
        self.ui.BrowseButton_2.clicked.connect(lambda: self.browse(self.ImageObjectTwo,self.ui.Imagelbl_3,2))
        logging.basicConfig(filename="MainLogFile.log",level=logging.INFO, format='%(asctime)s %(message)s', filemode='w')
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG) 
        

    def browse(self,ob,m,n):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file','',"Image files (*.jpg *.png *jpeg)")
        self.imgreading=cv2.imread(self.filename,1)
        self.qimg=cv2.cvtColor(self.imgreading,cv2.COLOR_BGR2GRAY)
        
        
        if (n==1):
                ob.imgPath=self.qimg
                pixmap = QtGui.QPixmap(self.filename)
                self.imgsize1=QImage(self.filename)
                self.width1 = QImage.width(self.imgsize1)
                self.height1 = QImage.height(self.imgsize1)
                print("image size 1 is",self.height1,"x",self.width1)
                pic=pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
                m.setPixmap(pic)
        
        if (n==2):
                ob.imgPath=self.qimg
                pixmap = QtGui.QPixmap(self.filename)
                self.imgsize2=QImage(self.filename)
                self.width2= QImage.width(self.imgsize2)
                self.height2= QImage.height(self.imgsize2)
                print("image size 2 is",self.height2,"x",self.width2)
                if self.height2==self.height1 and self.width2==self.width1:
                    pic=pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
                    m.setPixmap(pic)
                else:
            
                    msgbox = QMessageBox()
                    msgbox.setIcon(QMessageBox.Warning)
                    msgbox.setWindowTitle('WARNING')
                    msgbox.setText('Only images of same sizes are allowed!')
                    msgbox.setStandardButtons(QMessageBox.Ok)
                    msgbox.exec_()
                    logging.info('Size doesnt match')
            
        logging.info('Opened Image :{}'.format(self.filename))
        
    def changeValue(self,value): 
        self.MagorRealslidervalue =self.PhaseorImaginartvalue= float(value)/10
        if self.sender() == self.ui.MagandPhaseSlider:
            
            print ("slidervalue1=",self.MagorRealslidervalue)
        elif self.sender()== self.ui.RealandImagSlider:
            
            print("slidervalue2",self.PhaseorImaginartvalue)
            
    def messageboximage(self):
                    msgbox = QMessageBox()
                    msgbox.setIcon(QMessageBox.Warning)
                    msgbox.setWindowTitle('WARNING')
                    msgbox.setText('Please Enter an Image!')
                    msgbox.setStandardButtons(QMessageBox.Ok)
                    msgbox.exec_()
                    logging.info('No Image Found')
    def combofftchanger(self,x):
        if self.filename:
            if (x==1):                
                if self.ui.comboBox.currentText()=="Magnitude":
                    self.ImageObjectOne.MagnitudeFT(self.ui.Imagelbl_2)
                elif self.ui.comboBox.currentText()=="Phase":
                    self.ImageObjectOne.PhaseFT(self.ui.Imagelbl_2)
                elif self.ui.comboBox.currentText()=="Imaginary":
                    self.ImageObjectOne.ImaginaryFT(self.ui.Imagelbl_2)
                elif self.ui.comboBox.currentText()=="Real":
                    self.ImageObjectOne.RealFT(self.ui.Imagelbl_2)
            if (x==2):
                if self.ui.comboBox_2.currentText()=="Magnitude":
                    self.ImageObjectTwo.MagnitudeFT(self.ui.Imagelbl_4)
                elif self.ui.comboBox_2.currentText()=="Phase":
                    self.ImageObjectTwo.PhaseFT(self.ui.Imagelbl_4)
                elif self.ui.comboBox_2.currentText()=="Imaginary":
                    self.ImageObjectTwo.ImaginaryFT(self.ui.Imagelbl_4)
                elif self.ui.comboBox_2.currentText()=="Real":
                    self.ImageObjectTwo.RealFT(self.ui.Imagelbl_4)
            logging.info('FFT Component Showed : FFTImage1 is selected {} FFTImage2 is selected {}'.format(self.ui.comboBox.currentText(),self.ui.comboBox_2.currentText()))
    
        else:
            self.messageboximage()
        
    
    def ImageChanger(self,n):
        if self.filename:
            if(n==1):
                if (self.ui.comboBox_5.currentText()=="Image 1"):
                    self.imageToBeMixed=self.ImageObjectOne
                if (self.ui.comboBox_5.currentText()=="Image 2"):
                    self.imageToBeMixed=self.ImageObjectTwo
            elif(n==2):
                if (self.ui.comboBox_6.currentText()=="Image 1"):
                    self.imageNotmix=self.ImageObjectOne
                if (self.ui.comboBox_6.currentText()=="Image 2"):
                    self.imageNotmix=self.ImageObjectTwo
            logging.info('image Selection : Image1 is selected {} Image2 is selected {}'.format(self.ui.comboBox_5.currentText(),self.ui.comboBox_6.currentText()))
        else:
            self.messageboximage()
    
    def messageboxmixes(self):
                    msgbox = QMessageBox()
                    msgbox.setIcon(QMessageBox.Warning)
                    msgbox.setWindowTitle('WARNING')
                    msgbox.setText('Valid Mixes are either Magnitude with Phase,UniformPhase,UniformMagnitude or Real with Imaginary!')
                    msgbox.setStandardButtons(QMessageBox.Ok)
                    msgbox.exec_()
                    logging.info('Invalid Mixing')
    def ComboBoxes7and8(self,n):
        if self.filename:
            if((self.ui.comboBox_7.currentText()=="Magnitude") or (self.ui.comboBox_7.currentText()=="Phase") or (self.ui.comboBox_7.currentText()=="Uniform Magnitude") or (self.ui.comboBox_7.currentText()=="Uniform Phase"))and ((self.ui.comboBox_8.currentText()=="Real") or (self.ui.comboBox_8.currentText()=="Imaginary")):
                self.messageboxmixes()
            if((self.ui.comboBox_8.currentText()=="Magnitude") or (self.ui.comboBox_8.currentText()=="Phase") or (self.ui.comboBox_8.currentText()=="Uniform Magnitude") or (self.ui.comboBox_8.currentText()=="Uniform Phase"))and ((self.ui.comboBox_7.currentText()=="Real") or (self.ui.comboBox_7.currentText()=="Imaginary")):
                self.messageboxmixes()     
            if (n==1):
                    if(self.ui.comboBox_7.currentText()=="Magnitude"):
                        self.modeone="Magnitude"
                    if(self.ui.comboBox_7.currentText()=="Phase"):
                        self.modeone="Phase"
                    if(self.ui.comboBox_7.currentText()=="Real"):
                        self.modeone="Real"
                    if(self.ui.comboBox_7.currentText()=="imaginary"):
                        self.modeone="imaginary"
                    if(self.ui.comboBox_7.currentText()=="Uniform Magnitude"):
                        self.modeone="UniformMagnitude"
                    if(self.ui.comboBox_7.currentText()=="Uniform Phase"):
                        self.modeone="UniformPhase"
            if (n==2):
                    if(self.ui.comboBox_8.currentText()=="Magnitude"):
                        self.modetwo="Magnitude"
                    if(self.ui.comboBox_8.currentText()=="Phase"):
                        self.modetwo="Phase"
                    if(self.ui.comboBox_8.currentText()=="Real"):
                        self.modetwo="Real"
                    if(self.ui.comboBox_8.currentText()=="imaginary"):
                        self.modetwo="imaginary"
                    if(self.ui.comboBox_8.currentText()=="Uniform Magnitude"):
                        self.modetwo="UniformMagnitude"
                    if(self.ui.comboBox_8.currentText()=="Uniform Phase"):
                        self.modetwo="UniformPhase"
            if(self.modeone=="Magnitude" or self.modeone=="Real" or self.modeone=="Uniform Magnitude"):
                    self.magOrRealratio=self.MagorRealslidervalue
                    self.phaseOrImgratio=100-self.MagorRealslidervalue
            elif(self.modeone=="Phase" or self.modeone=="imaginary" or self.modeone=="Uniform Phase" ):
                    self.magOrRealratio=100-self.MagorRealslidervalue
                    self.phaseOrImgratio=self.PhaseorImaginartvalue
            logging.info('Component Selection : Component 1 is selected {} Component 2 is selected {}'.format(self.ui.comboBox_7.currentText(),self.ui.comboBox_8.currentText()))
        else:
            self.messageboximage()            

    def ModesCheck(self):
        if (self.modeone=="Magnitude"):
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio), self.mode.magnitudeAndPhase)
        elif(self.modetwo=="Magnitude"):            
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio), self.mode.magnitudeAndPhase)
        elif(self.modeone=="Real"):
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio), self.mode.realAndImaginary)
        elif(self.modetwo=="Real"):
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio), self.mode.realAndImaginary)
        if((self.modeone=="UniformMagnitude" and self.modetwo=="UniformPhase") or (self.modeone=="UniformPhase" and self.modetwo=="UniformMagnitude")):
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio),self.mode.uniformMagnitudeandPhase)
        if(self.modeone=="UniformMagnitude" and self.modetwo=="Phase"):
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio),self.mode.uniformMagnitude)
        if(self.modeone=="UniformPhase" and self.modetwo=="Magnitude"):
            self.mixout=self.imageNotmix.mix(self.imageToBeMixed,float(self.magOrRealratio),float(self.phaseOrImgratio),self.mode.uniformPhase)
        logging.info('Parameters That  Will Be Mixed : {} {}  {} {}'.format(self.imageToBeMixed,self.magOrRealratio,self.phaseOrImgratio,self.modeone))
    def outputup(self):
        if self.filename:
            self.ModesCheck()
            if(self.ui.comboBox_3.currentText()=="Output One"):
                yourQImage=qimage2ndarray.array2qimage(self.mixout)
                pixmap = QPixmap(QPixmap.fromImage(yourQImage))
                self.PlotImage=pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
                self.ui.Imagelbl_5.setPixmap(self.PlotImage)
            elif(self.ui.comboBox_3.currentText()=="Output Two"):
                yourQImage=qimage2ndarray.array2qimage(self.mixout)
                pixmap = QPixmap(QPixmap.fromImage(yourQImage))
                self.PlotImage=pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
                self.ui.Imagelbl_6.setPixmap(self.PlotImage)
            logging.info('Output Selection : Output1 is selected {} '.format(self.ui.comboBox_3.currentText()))
                        
            logging.info('Output Mix generated : {} {}  {} {}'.format(self.magOrRealratio,self.modeone,self.phaseOrImgratio,self.modetwo))
        else:
            self.messageboximage()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
    
    