import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
import cv2
from keras.models import load_model
import glob
note = ""

def etape4():
    model = load_model('/home/jabrane/Downloads/pfa/project/recognition/model_02/model_02.h5')

    images = []
    nn = []
    for filename in glob.glob('/home/jabrane/Downloads/pfa/project/noteFinal/note_0*.png'):
        nn.append(filename)
    nn.sort()

    for fichier in nn:
        img = cv2.imread(fichier, 0)
        images.append(img)

    for file in os.listdir('/home/jabrane/Downloads/pfa/project/noteFinal/'):
        if file.endswith('.png'):
            os.remove('/home/jabrane/Downloads/pfa/project/noteFinal/'+file)

    noteFinal = ""
    for img in images:
        img = img.reshape(1,1,28,28).astype('float32')
        img = img / 255
        prediction = model.predict_classes(img)
        noteFinal = noteFinal + str(prediction[0])

    if len(images) > 2:
        print("Note final = " + noteFinal[0:2] + ","+ noteFinal[2:] + "/20")
        note = noteFinal[0:2] + ","+ noteFinal[2:] + "/20"
    else:
        print("Note final = " + noteFinal + "/20")
        note = noteFinal + "/20"
    
    return note

