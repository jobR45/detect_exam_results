import cv2

for i in range(1,7):
    im = cv2.imread('/home/medamine/Desktop/project/preProcessing/papier_0'+str(i)+'.png', cv2.IMREAD_GRAYSCALE)
    im = cv2.resize(im,(600,800))
    cv2.imwrite('papier_0'+str(i)+'.png', im)