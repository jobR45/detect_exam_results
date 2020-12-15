import cv2
import numpy as np
import math
from scipy import ndimage
from PIL import Image
import glob
import os, os.path
import matplotlib.pyplot as plt

def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)
    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty

def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted

def etape3():
    image_list = []
    nn = []
    nb = []
    for filename in glob.glob('/home/jabrane/Downloads/pfa/project/Notes/digit*.png'):
        nn.append(filename.split('.'))
    for i in range(0,len(nn)):
        nb.append(int(nn[i][0][48:]))
    nb.sort() 

    #print(nb)
    for number in nb:  
        gray = cv2.imread('/home/jabrane/Downloads/pfa/project/Notes/digit'+str(number)+'.png', cv2.IMREAD_GRAYSCALE)    
        image_list.append(gray)
        
    for file in os.listdir('/home/jabrane/Downloads/pfa/project/Notes/'):
        if file.endswith('.png'):
      
            os.remove('/home/jabrane/Downloads/pfa/project/Notes/'+file)
    i=0
    for gray in image_list:
        gray = cv2.resize(255-gray, (28, 28))  # 255-gray for inverting black and white
        (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        flatten = gray.flatten() / 255.0

        while np.sum(gray[0]) == 0:
            gray = gray[1:]

        while np.sum(gray[:,0]) == 0:
            gray = np.delete(gray,0,1)

        while np.sum(gray[-1]) == 0:
            gray = gray[:-1]

        while np.sum(gray[:,-1]) == 0:
            gray = np.delete(gray,-1,1)

        rows,cols = gray.shape
        if rows > cols:
            factor = 20.0/rows
            rows = 20
            cols = int(round(cols*factor))
            gray = cv2.resize(gray, (cols,rows))
        else:
            factor = 20.0/cols
            cols = 20
            rows = int(round(rows*factor))
            gray = cv2.resize(gray, (cols, rows))

        colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
        rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
        gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

        shiftx,shifty = getBestShift(gray)
        shifted = shift(gray,shiftx,shifty)
        gray = shifted
        cv2.imwrite("/home/jabrane/Downloads/pfa/project/noteFinal/note_0"+str(i)+".png", gray)
        i=i+1  