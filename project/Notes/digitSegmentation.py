import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def etape2():
        im = cv2.imread("/home/jabrane/Downloads/pfa/project/Notes/note_0.png", cv2.IMREAD_GRAYSCALE)
        
        for file in os.listdir('/home/jabrane/Downloads/pfa/project/Notes/'):
                if file.endswith('/home/jabrane/Downloads/pfa/project/Notes/'+file):
                        os.remove(file)
                
        (thresh, gray) = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        gray = 255 - gray

        (_, ctrs, hier) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        rects = [cv2.boundingRect(ctr) for ctr in ctrs]

        i = 0
        for rect in rects:
                x = rect[0]
                y = rect[1]
                w = rect[2]
                h = rect[3]
                crop_im = im[y:y+h, x:x+w]
                
                if (w >= 8 and w <= 20) and (h >= 15 and h <= 40) and y < 50:
                        cv2.imwrite("/home/medamine/Desktop/pfa/project/Notes/digit"+str(x)+".png", crop_im)
                        i = i+1
