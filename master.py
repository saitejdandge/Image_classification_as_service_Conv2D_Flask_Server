import os
from subprocess import call
from google_images_download import google_images_download

# script="python -m scripts.retrain \ --bottleneck_dir=tf_files/bottlenecks \ --how_many_training_steps=500 \ --model_dir=tf_files/models/ \ --summaries_dir=tf_files/training_summaries/\"${ARCHITECTURE}\" \ --output_graph=tf_files/retrained_graph.pb \ --output_labels=tf_files/retrained_labels.txt \ --architecture=\"${ARCHITECTURE}\" \ --image_dir=tf_files/downloads"




# #choice=input("1.Create New Project\n2.Use Existing Project\n");
# def modifyScript(project_name):
# 	script="python -m scripts.retrain \ --bottleneck_dir="+project_name+"/tf_files/bottlenecks \ --how_many_training_steps=500 \ --model_dir="+project_name+"/tf_files/models/ \ --summaries_dir="+project_name+"/tf_files/training_summaries/\"${ARCHITECTURE}\" \ --output_graph=tf_files/retrained_graph.pb \ --output_labels="+project_name+"/tf_files/retrained_labels.txt \ --architecture=\"${ARCHITECTURE}\" \ --image_dir="+project_name+"/tf_files/downloads"
# 	return script

def predict(project_name,file_name):
	os.system("ipython keras_scripts/predict.py "+project_name+" "+file_name)
	pass

def preprocess(project_name):
	os.system("ipython keras_scripts/preprocess.py "+project_name)
	pass

def trainModel(project_name):
	os.system("ipython keras_scripts/model.py "+project_name)
	pass

#rest call
def createDataset(keywords):
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":keywords,"limit":30} #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	print("Images Dataset scraped from google")
	# print(os.getcwd())
	print(os.getcwd())

	pass




def main(project_name):

	preprocess(project_name)
	trainModel(project_name)
	pass








