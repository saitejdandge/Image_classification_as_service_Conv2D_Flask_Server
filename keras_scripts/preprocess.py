import matplotlib.image as mpimg
import os
from PIL import Image
import numpy as np
import PIL
import sys
import matplotlib.pyplot as plt
from utils import *
import os

original_data_dir  = sys.argv[1]

base_folder=os.path.basename(original_data_dir)

print(original_data_dir)

img_height=img_width=300

squared_dir=original_data_dir

print(squared_dir)

print("Rescaling Images to dimension ",str(img_width)+" X "+str(img_height))

x=[]

y=[]

print("Converting Images to Arrays")
   
for subdir, dirs, files in os.walk(original_data_dir):
   
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg") or filepath.endswith('png') :

        	class_name=os.path.basename(os.path.dirname(filepath))

        	square_image(filepath,img_width,img_height)

        	read_image(filepath,class_name,x,y)


x=np.array(x)

y=np.array(y)


print("One hot encoding labels")

le,y=convert_to_one_hot(y,original_data_dir)

print("Saving X, Y objects locally")

set_value('x',x,original_data_dir)

set_value('y',y,original_data_dir)

print("Finished X, Y objects locally")

print('mapping ',get_value('mapping',original_data_dir))

print('x shape',get_value('x',original_data_dir).shape)

print('y shape',get_value('y',original_data_dir).shape)

print("Finished Preprocessing, Run model.py and select folder.")






