import cv2
import numpy as np
from  tkinter import Tk
from pathlib import Path
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
img_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
image = cv2.imread(img_path,1) # the work folder is the one displayed on the terminal
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 0, 255, 100)
res = 255 - edged
cv2.imshow("Edged", res)
cv2.waitKey(0)
cv2.imwrite('res.bmp', res)

# ctr = [[519, 269],
# 	   [520, 268],
# 	   [1099, 268],
# 	   [1100, 269],
# 	   [1100,644],
# 	   [1099, 645],
# 	   [520, 645],
# 	   [519, 644]]

# dwg = ezdxf.new('R2010')
# msp = dwg.modelspace()
# dwg.layers.new(name = 'MyLines', dxfattribs = {'color': 3})
# for i in range(len(ctr)):
# 	n = i + 1
# 	if n >= len(ctr):
# 		n = 0
# 	msp.add_line(ctr[i], ctr[n], dxfattribs = {'layer' : 'MyLines'})
# 	print(ctr[i], '->', ctr[n])
# 	dwg.saveas('line.dxf')
