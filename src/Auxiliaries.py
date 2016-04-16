import pygame, os

def readImagePathList():
	paths = open("../img/paths.txt","r")
	pathlist = {}
	
	lines = paths.readlines()
	paths.close()
	
	#write lines in the dictionary
	i = 0
	while (i < len(lines)):
		
		#ignore empty lines
		if(not lines[i]=="\n"):
			#remove newline at the end of the lines
			pathlist.update({lines[i][:-1]:lines[i+1][:-1]})

		i = i+2
	
	return pathlist
