import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def etap1(File):
        im = cv2.imread(File, cv2.IMREAD_GRAYSCALE)
        (thresh, gray) = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = 255 - gray
        (_,ctrs, hier) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        rects = [cv2.boundingRect(ctr) for ctr in ctrs]
        j=0
        for rect in rects:
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]
                crop_im = im[y:y+h, x:x+w]
                
                if (w >= 50 and w <= 100) and (h >= 80 and h <= 120) and (x<=30 and x>=20):
                        cv2.imwrite('/home/jabrane/Downloads/pfa/project/Notes/note_'+str(j)+'.png', crop_im)
                        break
                        j=j+1
    
