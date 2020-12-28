# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\hw1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 1. SIFT
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        # 2. Calibration
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 3. Augmented Reality
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # 4. Stereo Disparity Map
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        # 5. Training Cifar10 Classifier Using VGG16
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 230, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")  
        

        # layout of 2
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 350, 341, 260))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")


        self.btn2_1 = QtWidgets.QPushButton(self.frame)
        self.btn2_1.setGeometry(QtCore.QRect(10, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn2_1.setFont(font)
        self.btn2_1.setObjectName("btn2_1")

        self.btn2_2 = QtWidgets.QPushButton(self.frame)
        self.btn2_2.setGeometry(QtCore.QRect(10, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn2_2.setFont(font)
        self.btn2_2.setObjectName("btn2_2")

        self.btn2_4 = QtWidgets.QPushButton(self.frame)
        self.btn2_4.setGeometry(QtCore.QRect(10, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn2_4.setFont(font)
        self.btn2_4.setObjectName("btn2_4")

        # layout of 2.3
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(160, 70, 171, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")

        self.btn2_3 = QtWidgets.QPushButton(self.frame_2)
        self.btn2_3.setGeometry(QtCore.QRect(30, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn2_3.setFont(font)
        self.btn2_3.setObjectName("btn2_3")

        # 2.3 select image
        self.label_2_3_S = QtWidgets.QLabel(self.frame_2)
        self.label_2_3_S.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2_3_S.setFont(font)
        self.label_2_3_S.setObjectName("label_2_3_S")

        # 2.3 Drop-down menu
        self.cboxImgNum = QtWidgets.QComboBox(self.frame_2)
        self.cboxImgNum.setGeometry(QtCore.QRect(10, 50, 151, 31))
        self.cboxImgNum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cboxImgNum.setObjectName("cboxImgNum")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")
        self.cboxImgNum.addItem("")

        # 2.3 Extrinsic button
        self.label_2_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_2_3.setGeometry(QtCore.QRect(200, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2_3.setFont(font)
        self.label_2_3.setObjectName("label_2_3")

        # layout of 3 
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(410, 70, 271, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")

        # layout of button3.1
        self.btn3_1 = QtWidgets.QPushButton(self.frame_3)
        self.btn3_1.setGeometry(QtCore.QRect(25, 5, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn3_1.setFont(font)
        self.btn3_1.setObjectName("btn3_1")

        # layout of 4
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(410, 180, 271, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")

        ## layout of button4.1
        self.btn4_1 = QtWidgets.QPushButton(self.frame_4)
        self.btn4_1.setGeometry(QtCore.QRect(25, 5, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn4_1.setFont(font)
        self.btn4_1.setObjectName("btn4_1")

        # layout of 1 
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(50, 60, 341, 260))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")

        # layout of button1.1
        self.btn1_1 = QtWidgets.QPushButton(self.frame_5)
        self.btn1_1.setGeometry(QtCore.QRect(65, 5, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn1_1.setFont(font)
        self.btn1_1.setObjectName("btn1_1")

        # layout of button1.2
        self.btn1_2 = QtWidgets.QPushButton(self.frame_5)
        self.btn1_2.setGeometry(QtCore.QRect(65, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn1_2.setFont(font)
        self.btn1_2.setObjectName("btn1_2")

        # layout of label 1.2 count of coim01  
        self.label_1_2_01 = QtWidgets.QLabel(self.frame_5)
        self.label_1_2_01.setGeometry(QtCore.QRect(65, 135, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_1_2_01.setFont(font)
        self.label_1_2_01.setObjectName("label_1_2_01")

        # layout of label 1.2 count of coim02 
        self.label_1_2_02 = QtWidgets.QLabel(self.frame_5)
        self.label_1_2_02.setGeometry(QtCore.QRect(65, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_1_2_02.setFont(font)
        self.label_1_2_02.setObjectName("label_1_2_02")

        # layout of 5 
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(410, 260, 271, 400))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")

        # layout of button5.1
        self.btn5_1 = QtWidgets.QPushButton(self.frame_6)
        self.btn5_1.setGeometry(QtCore.QRect(25, 5, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn5_1.setFont(font)
        self.btn5_1.setObjectName("btn5_1")

        # layout of button5.2
        self.btn5_2 = QtWidgets.QPushButton(self.frame_6)
        self.btn5_2.setGeometry(QtCore.QRect(25, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn5_2.setFont(font)
        self.btn5_2.setObjectName("btn5_2")

        # layout of button5.3
        self.btn5_3 = QtWidgets.QPushButton(self.frame_6)
        self.btn5_3.setGeometry(QtCore.QRect(25, 140, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn5_3.setFont(font)
        self.btn5_3.setObjectName("btn5_3")

        # layout of button5.4
        self.btn5_4 = QtWidgets.QPushButton(self.frame_6)
        self.btn5_4.setGeometry(QtCore.QRect(25, 305, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn5_4.setFont(font)
        self.btn5_4.setObjectName("btn5_4")

        # layout of SpinBox to 5.3
        self.SpinBox5 = QtWidgets.QSpinBox(self.frame_6)
        self.SpinBox5.setGeometry(QtCore.QRect(50, 95, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.SpinBox5.setFont(font)
        self.SpinBox5.setRange(1, 12503)
        self.SpinBox5.setObjectName("SpinBox5")

        # 5.3 select image
        self.label_5_3 = QtWidgets.QLabel(self.frame_6)
        self.label_5_3.setGeometry(QtCore.QRect(10, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5_3.setFont(font)
        self.label_5_3.setObjectName("label_5_3")

        # layout of SpinBox to 5.4
        self.SpinBoxNo = QtWidgets.QSpinBox(self.frame_6)
        self.SpinBoxNo.setGeometry(QtCore.QRect(50, 185, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.SpinBoxNo.setFont(font)
        self.SpinBoxNo.setRange(1, 12503)
        self.SpinBoxNo.setObjectName("SpinBoxNo")

        # 5.4 select image
        self.label_5_4_no = QtWidgets.QLabel(self.frame_6)
        self.label_5_4_no.setGeometry(QtCore.QRect(10, 195, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5_4_no.setFont(font)
        self.label_5_4_no.setObjectName("label_5_4_no")

        # layout of SpinBox to 5.4
        self.SpinBoxH = QtWidgets.QSpinBox(self.frame_6)
        self.SpinBoxH.setGeometry(QtCore.QRect(50, 225, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.SpinBoxH.setFont(font)
        self.SpinBoxH.setRange(1, 224)
        self.SpinBoxH.setObjectName("SpinBoxH")

        # 5.4 image height
        self.label_5_4_H = QtWidgets.QLabel(self.frame_6)
        self.label_5_4_H.setGeometry(QtCore.QRect(10, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5_4_H.setFont(font)
        self.label_5_4_H.setObjectName("label_5_4_H")

        # layout of SpinBox to 5.4
        self.SpinBoxW = QtWidgets.QSpinBox(self.frame_6)
        self.SpinBoxW.setGeometry(QtCore.QRect(50, 265, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.SpinBoxW.setFont(font)
        self.SpinBoxW.setRange(1, 224)
        self.SpinBoxW.setObjectName("SpinBoxW")

        # 5.4 image weight
        self.label_5_4_W = QtWidgets.QLabel(self.frame_6)
        self.label_5_4_W.setGeometry(QtCore.QRect(10, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5_4_W.setFont(font)
        self.label_5_4_W.setObjectName("label_5_4_W")

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn3_1.setText(_translate("MainWindow", "3.1 Augmented Reality"))
        self.btn4_1.setText(_translate("MainWindow", "4.1 Stereo Disparity Map"))
        self.btn1_1.setText(_translate("MainWindow", "1.1 Draw Contour"))
        self.btn1_2.setText(_translate("MainWindow", "1.2 Count Coins"))
        self.btn5_1.setText(_translate("MainWindow", "5.1 Show epochs"))
        self.btn5_2.setText(_translate("MainWindow", "5.2 Show final screenshot of TensorBoard "))
        self.btn5_3.setText(_translate("MainWindow", "5.3 Select a picture to be classification"))
        self.btn5_4.setText(_translate("MainWindow", "5.4 Resize a picture to be classification"))
        self.label.setText(_translate("MainWindow", "2. Calibration"))
        self.label_3.setText(_translate("MainWindow", "3. Augmented Reality"))
        self.label_4.setText(_translate("MainWindow", "4. Stereo Disparity Map"))
        self.label_1.setText(_translate("MainWindow", "1. SIFT"))
        self.label_1_2_01.setText(_translate("MainWindow", "There are __ coins in coin01.jpg"))
        self.label_1_2_02.setText(_translate("MainWindow", "There are __ coins in coin02.jpg"))
        self.label_3.setText(_translate("MainWindow", "3. Augmented Reality"))
        self.label_5.setText(_translate("MainWindow", "5. Cifar10 Classifier"))
        self.btn2_2.setText(_translate("MainWindow", "2.2 Find Intrinsic"))
        self.btn2_1.setText(_translate("MainWindow", "2.1 Find Corners"))
        self.btn2_4.setText(_translate("MainWindow", "2.4 Find Distortion"))
        self.btn2_3.setText(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.label_2_3_S.setText(_translate("MainWindow", "Select Image"))
        self.label_5_3.setText(_translate("MainWindow", "Image"))
        self.label_5_4_no.setText(_translate("MainWindow", "Image"))
        self.label_5_4_H.setText(_translate("MainWindow", "Height"))
        self.label_5_4_W.setText(_translate("MainWindow", "Weight"))
        self.cboxImgNum.setItemText(0, _translate("MainWindow", "1"))
        self.cboxImgNum.setItemText(1, _translate("MainWindow", "2"))
        self.cboxImgNum.setItemText(2, _translate("MainWindow", "3"))
        self.cboxImgNum.setItemText(3, _translate("MainWindow", "4"))
        self.cboxImgNum.setItemText(4, _translate("MainWindow", "5"))
        self.cboxImgNum.setItemText(5, _translate("MainWindow", "6"))
        self.cboxImgNum.setItemText(6, _translate("MainWindow", "7"))
        self.cboxImgNum.setItemText(7, _translate("MainWindow", "8"))
        self.cboxImgNum.setItemText(8, _translate("MainWindow", "9"))
        self.cboxImgNum.setItemText(9, _translate("MainWindow", "10"))
        self.cboxImgNum.setItemText(10, _translate("MainWindow", "11"))
        self.cboxImgNum.setItemText(11, _translate("MainWindow", "12"))
        self.cboxImgNum.setItemText(12, _translate("MainWindow", "13"))
        self.cboxImgNum.setItemText(13, _translate("MainWindow", "14"))
        self.cboxImgNum.setItemText(14, _translate("MainWindow", "15"))
        self.label_2_3.setText(_translate("MainWindow", "2.3 Extrinsic"))
