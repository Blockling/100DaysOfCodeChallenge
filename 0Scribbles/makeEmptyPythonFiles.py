#Make a for loop that runs a hundred times and creates empty .py files named 1-100.py that can be used for scribbling
import os

#brick the program so that the scribbles will not be deleted
while True:
	print("This is a brick")

# Specify the directory path
path = r'C:\Users\ezged\Documents\GitHub\100DaysOfCodeChallenge\0Scribbles'


for file in range(0, 100):	#runs 100 times
	# Creating a file at specified folder
	# join directory and file path
	file_name = "scribble"+str(file)+".py"
	with open(os.path.join(path, file_name), 'w') as fp:
	# uncomment below line if you want to create an empty file
		fp.write('This is a new line')
	







