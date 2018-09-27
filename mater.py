import os

print("Hello welcome to Pixel, Image classification as service")


choice=input("1.Create New Project\n2.Use Existing Project")
print("chosen choice is "+choice)
def createProject():

	project_name=input("Please enter project name")
	os.mkdir(project_name)

	pass


if choice=="1":
	createProject()
	pass
if choice=="2":
	existing()
	pass