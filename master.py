import os
import json
from google_images_download import google_images_download
print("Hello welcome to Pixel, Image classification as service\n\n")


#choice=input("1.Create New Project\n2.Use Existing Project\n");

#rest call
def createDataset():
	record_count=int(input("Enter number of classes"))
	records=""
	count=0
	for x in range(0,record_count):
		records=records+input("enter keyword \n")
		if count!=record_count-1:
			records=records+","
			pass
		pass
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":records,"limit":10} #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	
	pass

#rest call with project_name 
def createProject():

	project_name=input("Please enter project name\n")
	os.mkdir(project_name)
	os.chdir(project_name)
	createDataset()
	pass

createProject()

# if choice=="1":
# 	createProject()
# 	pass
# if choice=="2":
# 	existing()
# 	pass