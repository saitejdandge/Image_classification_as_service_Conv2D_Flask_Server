
from keras.models import load_model
from utils import *
import matplotlib.image as mpimg

import sys

def main():

	print("prediction started")

	original_data_dir  = sys.argv[1]

	print(original_data_dir+'/model_data/model.h5')

	model=load_model(original_data_dir+'/model_data/model.h5')

	filename=sys.argv[2]

	squared_image=square_image(filename,300,300)

	x=mpimg.imread(squared_image)

	x=x[:,:,:3] #removing alpha channel

	x=x.reshape([1,x.shape[0],x.shape[1],x.shape[2]])

	prediction= convert_to_labels(model.predict(x),original_data_dir)[0]
	
	print("prediction is "+prediction)
	
	return  str(prediction)
	pass

main()

