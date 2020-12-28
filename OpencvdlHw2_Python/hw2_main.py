# -*- coding: utf-8 -*-

import sys
import pylab
import matplotlib.pyplot as plt
import cv2 as cv
import keras.backend as K
import pandas as pd
import numpy as np
import glob
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib import pyplot as plt
from keras.datasets import cifar10
from keras.models import load_model ,model_from_json
from keras.utils import to_categorical
from hw2_ui import Ui_MainWindow
from keras.preprocessing.image import ImageDataGenerator,load_img ,img_to_array
from sklearn.model_selection import train_test_split
from keras.models import load_model

cont4 = 0
coin01num = 0
coin02num = 0
machingKpoint1 = 0
machingKpoint2 = 0
img4_match = 0
list_keypoints1 = []
list_keypoints2 = []
model = load_model('./OpencvdlHw2_Python/final_ResNet50_model.h5')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    def onBindingUI(self):
        self.btn1_1.clicked.connect(self.on_btn1_1_click)
        self.btn1_2.clicked.connect(self.on_btn1_2_click)
        self.btn2_1.clicked.connect(self.on_btn2_1_click)
        self.btn2_2.clicked.connect(self.on_btn2_2_click)
        self.btn2_3.clicked.connect(self.on_btn2_3_click)
        self.btn2_4.clicked.connect(self.on_btn2_4_click)
        self.btn3_1.clicked.connect(self.on_btn3_1_click)
        self.btn4_1.clicked.connect(self.on_btn4_1_click)
        self.btn5_1.clicked.connect(self.on_btn5_1_click)
        self.btn5_2.clicked.connect(self.on_btn5_2_click)
        self.btn5_3.clicked.connect(self.on_btn5_3_click)
        self.btn5_4.clicked.connect(self.on_btn5_4_click)

    def on_btn1_1_click(self):
        coin01 = cv.imread("./Datasets/Q1_Image/coin01.jpg")
        coin02 = cv.imread("./Datasets/Q1_Image/coin02.jpg")
        cv.imshow('coin01',coin01)
        cv.imshow('coin02',coin02)
        # get binary image and apply Gaussian blur
        coin01_gray = cv.cvtColor(coin01, cv.COLOR_BGR2GRAY)
        coin01_preprocessed = cv.GaussianBlur(coin01_gray, (5, 5), 0)
        _, coin01_binary = cv.threshold(coin01_preprocessed, 130, 255, cv.THRESH_BINARY)

        coin02_gray = cv.cvtColor(coin02, cv.COLOR_BGR2GRAY)
        coin02_preprocessed = cv.GaussianBlur(coin02_gray, (5, 5), 0)
        _, coin02_binary = cv.threshold(coin02_preprocessed, 130, 255, cv.THRESH_BINARY)

        # invert image to get coins
        coin01_binary = cv.bitwise_not(coin01_binary)

        coin02_binary = cv.bitwise_not(coin02_binary)

        # morph coins by eroding and dilating to remove noise
        morph_kernel = np.ones((15,15),np.uint8)
        coin01_morph = cv.morphologyEx(coin01_binary, cv.MORPH_CLOSE, morph_kernel)

        coin02_morph = cv.morphologyEx(coin02_binary, cv.MORPH_CLOSE, morph_kernel)

        # find contours
        coin01_contours, _ = cv.findContours(coin01_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        coin02_contours, _ = cv.findContours(coin02_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # make copy of image
        coin01_and_contours = np.copy(coin01)

        coin02_and_contours = np.copy(coin02)

        # find contours of large enough area
        min_coin_area = 60
        coin01_large_contours = [cnt for cnt in coin01_contours if cv.contourArea(cnt) > min_coin_area]

        coin02_large_contours = [cnt for cnt in coin02_contours if cv.contourArea(cnt) > min_coin_area]

        # draw contours
        cv.drawContours(coin01_and_contours , coin01_large_contours, -1, (0,255,0))

        cv.drawContours(coin02_and_contours , coin02_large_contours, -1, (0,255,0))

        cv.imshow(" Draw Contours with Coin01",coin01_and_contours )
        cv.imshow(" Draw Contours with Coin02",coin02_and_contours )
        cv.waitKey(0)
        cv.destroyAllWindows()
        # print number of contours
        global coino1num 
        coino1num = len(coin01_large_contours)
        global coino2num 
        coino2num = len(coin02_large_contours)
        global cont4
        cont4 = 1

    def on_btn1_2_click(self):
        global cont4
        if  cont4 == 0 : 
            print('Please push 1.1 Draw Contours first')
        else :
            self.label_1_2_01.setText( "There are " + str(coino1num) + " coins in coin01.jpg")
            self.label_1_2_02.setText("There are " + str(coino2num) + " coins in coin02.jpg")


    def on_btn2_1_click(self):
        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        #read all the images from folder
        images= glob.glob("./Datasets/Q2_Image/*.bmp")

        i=0
        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (11,8),None)

            # If found, add object points, image points (after refining them)
            i=i+1
            if ret == True:
                objpoints.append(objp)
                corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv.drawChessboardCorners(img, (11,8), corners2,ret)

                cv.namedWindow(str(i),cv.WINDOW_GUI_NORMAL )
                cv.imshow(str(i),img)
                cv.waitKey(500)

        cv.destroyAllWindows()

    def on_btn2_2_click(self):
        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        #read all the images from folder
        images= glob.glob("./Datasets/Q2_image/*.bmp")

        i=0
        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (11,8),None)

            # If found, add object points, image points (after refining them)
            i=i+1
            if ret == True:
                objpoints.append(objp)
                corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        print(mtx)
        cv.waitKey(500)
        cv.destroyAllWindows()

    def on_btn2_3_click(self):
        # get the input from ui item
        number = int(self.cboxImgNum.currentText())

         # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        # read images
        path = './Datasets/Q2_image/'+ str(number)+'.bmp'
        img = cv.imread(path)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        print(path)
        # Find the chess board corners
        ret, corners = cv.findChessboardCorners(gray, (11,8),None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners2)
            ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

            # get rotation matrix and plus tranalation matrix
            R, jacobian = cv.Rodrigues(rvecs[0])
            extrinsic = np.hstack((R,tvecs[0]))
            print(extrinsic)


    def on_btn2_4_click(self):
        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (7,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        #read all the images from folder
        images = glob.glob("./Datasets/Q2_image/*.bmp")
        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (11,8),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)
                corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        print(dist)


    def on_btn3_1_click(self):
        # define criteria = (type,max_iter,epsilon)
        # cv.TERM_CRITERIA_EPS :The accuracy (error) meets the epsilon stop , accuracy = 0.001
        # cv.TERM_CRITERIA_MAX_ITER：The number of iterations exceeds max_iter stop ,max_iter = 30.
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images.
        objpoints = [] # 3d point in real world space
        imgpoints = [] # 2d points in image plane.

        #read all the images from folder
        images = glob.glob("./Datasets/Q3_image/*.bmp")

        for fname in images:
            img = cv.imread(fname)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (11,8),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)

                corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)

        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

        # Function to draw the axis
        def draw(img, corners, imgpts):
            imgpts = np.int32(imgpts).reshape(-1,2) 
            # draw ground floor in green(0,255,0)
            img = cv.drawContours(img, [imgpts[:4]],-1,(0,0,255),10)

            # draw pillars in blue color
            for i,j in zip(range(4),range(4,8)):
                img = cv.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(0,0,255),10)

            # draw top layer in red(0,0,255) color
            # img = cv.drawContours(img, [imgpts[4:]],-1,(0,0,255),10)
            return img

        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((8*11,3), np.float32)
        objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2)
        axis = np.float32([[1,1,0], [3,5,0], [3,5,0], [5,1,0],[3,3,-3],[3,3,-3],[3,3,-3],[3,3,-3] ])

        # declare a array to store video frame
        Video_img=[]
        for fname in glob.glob("./Datasets/Q3_image/*.bmp"):
            img = cv.imread(fname)
            gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            ret, corners = cv.findChessboardCorners(gray, (11,8),None)

            if ret == True:
                corners2 = cv.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

                # Find the rotation and translation vectors.
                _,rvecs, tvecs, inliers = cv.solvePnPRansac(objp, corners2, mtx, dist)

                # project 3D points to image plane
                imgpts, jac = cv.projectPoints(axis, rvecs, tvecs, mtx, dist)

                img = draw(img,corners2,imgpts)
                Video_img.append(img)
                cv.imshow('Video',img)
                cv.waitKey(500)

        # making vidoe
        height,width,layers=Video_img[1].shape
        video=cv.VideoWriter('video.mp4',-1,2,(width,height))
        for j in range(0,5):
            video.write(Video_img[j])

        cv.destroyAllWindows()


    def on_btn4_1_click(self):
        # read left and right images
        imgL = cv.imread("./Datasets/Q4_image/imgL.png",0)
        imgR = cv.imread("./Datasets/Q4_image/imgR.png",0)

        # making disparity map
        stereo = cv.StereoSGBM_create(numDisparities=16, blockSize=21) #the third parameter
        disparity = stereo.compute(imgL,imgR)

        # normalization

        normalized_img = cv.normalize(disparity, disparity, 0, 255, cv.NORM_MINMAX,cv.CV_8U)

        cv.imshow('Without L-R Disparity Check',normalized_img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
    def on_btn5_1_click(self):
        acc = cv.imread("./OpencvdlHw2_Python/5-1.jpg", cv.IMREAD_COLOR)
        cv.imshow('epochs',acc)
        model.summary()
        cv.waitKey(0)
        cv.destroyAllWindows()


    def on_btn5_2_click(self):
        acc = cv.imread("./OpencvdlHw2_Python/5-2.jpg", cv.IMREAD_COLOR)
        cv.imshow('TensorBoar',acc)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
    def on_btn5_3_click(self):
        i = int(self.SpinBox5.text())
        filename = "./test1/" +str(i)+".jpg"
        img = load_img(filename, target_size=(224, 224))
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 224, 224, 3)
        # center pixel data
        img = img.astype('float32')
        img = img - [123.68, 116.779, 103.939]
        result = model.predict(img)
        if(result >0.5):
            label = "Dog"
        else:
            label = "Cat"  
        image = plt.imread(filename)
        plt.title("Class: "+label)
        plt.imshow(image)
        pylab.show()    

    def on_btn5_4_click(self):
        No = int(self.SpinBoxNo.text())
        filename = "./test1/" +str(No)+".jpg"
        Height = int(self.SpinBoxH.text())
        Weight = int(self.SpinBoxW.text())
        img  = cv.imread(filename)
        img = cv.resize(img , (224,224))
        Rimg = cv.resize(img , (Height, Weight))
        # convert to array
        Arrimg = img_to_array(img)

        if  Height>224 and Weight>224:
            Rimg = cv.resize(img , (224, 224))
        elif Weight>224:
            Rimg = cv.resize(img , (Height, 224)) 
        elif Height>224:
             Rimg = cv.resize(img , (224, Weight))    

        ArrRimg = img_to_array(Rimg)
        Rimg = np.full_like((Arrimg), 0)
        Rimg [:ArrRimg.shape[0],:ArrRimg.shape[1]] =ArrRimg
        # reshape into a single sample with 3 channels
        img = img.reshape(1, 224, 224, 3)
        Rimg = Rimg.reshape(1, 224, 224, 3)
        # center pixel data
        img = img.astype('float32')
        Rimg = Rimg.astype('float32')
        img = img - [123.68, 116.779, 103.939]
        Rimg = Rimg - [123.68, 116.779, 103.939]
        # predict image
        result = model.predict(img)
        Rresult = model.predict(Rimg)
        OriginImg = cv.imread(filename)
        ResizeImg = cv.resize(OriginImg , (Height, Weight))
        fig, axs = plt.subplots(1, 2)
        axs[0].imshow(OriginImg)
        axs[0].set_title('OriginImg')
        axs[1].imshow(ResizeImg)
        axs[1].set_title('ResizeImg')
        pylab.show()

        votes=[float(result),float(Rresult)]           
        candidates=['Before resize', 'After resize'] 
        x=np.arange(len(candidates))  
        y=np.arange(0, 1, 0.2)  
        plt.bar(x, votes)        
        plt.xticks(x, candidates)     
        plt.yticks(y)      
        plt.title('Resize augmention comparion')  
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
