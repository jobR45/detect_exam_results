import tkinter as tk
from tkinter import Label
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import sqlite3 as lite
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/jabrane/Downloads/pfa')
from project import main

#Base connection
con = lite.connect('user.db')

note = ""
def suppImage():
    imageCanvas.delete("all")
    root.update()

def openImage():
    File = askopenfilename(
                title='Choose a file',
                filetypes=[('all files', '.*'),
                            ('text files', '.txt'),
                            ('image files', '.png;.jpg'),       
                            ('image files!', '*.png;*.jpg')])
    img = tk.PhotoImage(file=str(File))
    label = Label(image=img)
    label.image = img # keep a reference!
    imageCanvas.create_image(300,400,image=img, anchor="center")
    note = main.main(File)
    textWidget.insert(tk.END, note)
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO etudiant VALUES('"+note+"')")
    
def bounding():
        imageCanvas.create_line(26,344,93,344,93,428,26,428,26,344)

#Frames and canvas
root = tk.Tk()
root.title("Amine et Jigabo PFA")
frame = tk.Frame(root)
frame.pack()

buttonFrame = tk.Frame(root)
buttonFrame.pack( side = "right")

textWidget = tk.Text(buttonFrame, width = 13, height = 2)
textWidget.pack()

imageCanvas = tk.Canvas(width = 600, height = 800, bg = "white")
imageCanvas.pack()
#canvas = tk.Canvas(width = 400, height = 10, bg ="black")
#canvas.pack()
#Buttons
uploadButton = tk.Button(buttonFrame, text="Upload Image", width = 10, height = 2,command=openImage)
uploadButton.pack( side = "top")
deleteButton = tk.Button(buttonFrame, text="Delete Image", width = 10, height = 2,command=suppImage)
deleteButton.pack( side = "top")
startButton = tk.Button(buttonFrame, text="Start Recognition", fg="black",width = 10, height = 2)
startButton.pack( side = "top" )
quitButton = tk.Button(buttonFrame, text="Upload Base", fg="blue",width = 10, height = 2)
quitButton.pack( side = "top")
quitButton = tk.Button(buttonFrame, text="Quit", fg="blue",width = 10, height = 2, command=root.destroy)
quitButton.pack( side = "top")

root.mainloop()