import os

#this the path that where all changes will be made
#parent_path = r"C:\Users\Matthew\Desktop\Temp Inventor- Path breaker\405-3015_A"
#final_path = r"C:\Users\Matthew\Desktop\Temp Inventor- Path breaker\405-3012"
#os.chdir(parent_path)


#this function takes in a path, a string to replace and the replacment string
#it will find every file in every subdirectory and rename every file
def rename_files(path, original_string ,replacement_string):
	#get a list of every file and folder in the directory
	file_list = os.listdir(path)
	#set the current directory to the one you want to change to
	os.chdir(path)

	#rename every file in directory that has a matching string
	for file_name in file_list:
		if (file_name != "lockfile.lck") & (file_name !=  "OldVersions"):
			new_file_name = file_name.replace(original_string,replacement_string)
			os.rename(file_name, new_file_name)

	#get a new list of all files and folders		
	file_list = os.listdir(path)

	#this loop will check if there are any sub directories
	for file_name in file_list:
		#skip the subdirectory "OldVersions"
		if (file_name != "OldVersions"):
			#create a new path for each item
			child_path = path + "\\" +file_name
			#check if the path is a directory, if yes, call rename_files on the subdirecotry
			if(os.path.isdir(child_path)):
				print (child_path)
				rename_files(child_path,original_string,replacement_string)

	#once you get to the bottom of the tree, reset to the parent directory.
	os.chdir(os.path.dirname(path))
	print(os.getcwd())



#rename_files(parent_path, "3011", "3015")