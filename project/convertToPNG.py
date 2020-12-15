from PIL import Image
for i in range(1,7):
    im = Image.open('/home/medamine/Desktop/project/papierJPG/papier_0'+str(i)+'.jpg')
    im.save('/home/medamine/Desktop/project/papierPNG/papier_0'+str(i)+'.png')
