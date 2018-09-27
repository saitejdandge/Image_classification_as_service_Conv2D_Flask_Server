import os
from subprocess import call
from google_images_download import google_images_download

script="python -m scripts.retrain \ --bottleneck_dir=tf_files/bottlenecks \ --how_many_training_steps=500 \ --model_dir=tf_files/models/ \ --summaries_dir=tf_files/training_summaries/\"${ARCHITECTURE}\" \ --output_graph=tf_files/retrained_graph.pb \ --output_labels=tf_files/retrained_labels.txt \ --architecture=\"${ARCHITECTURE}\" \ --image_dir=tf_files/downloads"

print("Hello welcome to Pixel, Image classification as service\n\n")

project_name=""

#choice=input("1.Create New Project\n2.Use Existing Project\n");
def modifyScript(project_name):
	script="python -m scripts.retrain \ --bottleneck_dir="+project_name+"/tf_files/bottlenecks \ --how_many_training_steps=500 \ --model_dir="+project_name+"/tf_files/models/ \ --summaries_dir="+project_name+"/tf_files/training_summaries/\"${ARCHITECTURE}\" \ --output_graph=tf_files/retrained_graph.pb \ --output_labels="+project_name+"/tf_files/retrained_labels.txt \ --architecture=\"${ARCHITECTURE}\" \ --image_dir="+project_name+"/tf_files/downloads"
	return script

def trainModel(project_name):
	os.system("ipython keras-scripts/model.py "+project_name)
	pass

#rest call
def createDataset(project_name):

	record_count=int(input("Enter number of classes / labels\n"))
	records=""
	count=0
	for x in range(0,record_count):
		records=records+input("Enter keyword \n")
		if count!=record_count-1:
			records=records+","
			pass
		pass
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":records,"limit":1} #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	print("Images Dataset scraped from google")
	# print(os.getcwd())
	print(os.getcwd())
	os.chdir("..")
	print(os.getcwd())
	os.system("ipython keras-scripts/preprocess.py "+project_name)
	trainModel(project_name)
	pass



#rest call with project_name 
def createProject():

	project_name=input("Please enter project name\n")
	os.mkdir(project_name)
	os.chdir(project_name)
	createDataset(project_name)
	pass

createProject()

# if choice=="1":
# 	createProject()
# 	pass
# if choice=="2":
# 	existing()
# 	pass