from PIL import Image
import cv2
import numpy

for i in range(1,7):
    img = Image.open('/home/medamine/Desktop/project/papierPNG/papier_0'+str(i)+'.png')
    crop_img = img.crop((900,0,3250,2480))
    crop_img.save('/home/medamine/Desktop/project/preProcessing/papier_0'+str(i)+'.png')