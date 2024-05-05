from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2

images = []
paths = []
paths = filedialog.askopenfilenames(initialdir="/home/raz/src/indor/imagestitcher/Images", title="Select file",filetypes=(("JPEG",".jpg .jpeg"), ("PNG",".png")))

for p in paths:
    images.append(cv2.imread(p))

thumbs = []
for img in images:
    thumbs.append(cv2.resize(img, (800,800)))

path= "/home/raz/src/indor/imagestitcher/Images/thumbnails/"
for i, t in enumerate(thumbs):
    cv2.imwrite(path + str(i)+".png", t)

