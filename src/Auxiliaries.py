import pygame, os

def readImagePathList():
	paths = open("../img/paths.txt","r")
	pathlist = {}
	
	lines = paths.readlines()
	paths.close()
	
	# ignore leading spaces and tabstops
	for i in range(len(lines)):
		while (lines[i][0] == " " or lines[i][0] == "\t"):
			lines[i] = lines[i][1:]
	
	#write lines in the dictionary
	i = 0
	while (i < len(lines)):

		#ignore empty lines and comments
		if(lines[i]=="\n" or
				lines[i][0] == "#"):
			i += 1
			continue

		#remove newline at the end of the lines
		pathlist.update({lines[i][:-1]:lines[i+1][:-1]})

		i = i+2
	
	return pathlist
	
	
def readSoundPathList():
	paths = open("../sounds/pathsSound.txt","r")
	pathlist = {}
	
	lines = paths.readlines()
	paths.close()
	
	# ignore leading spaces and tabstops
	for i in range(len(lines)):
		while (lines[i][0] == " " or lines[i][0] == "\t"):
			lines[i] = lines[i][1:]
	
	#write lines in the dictionary
	i = 0
	while (i < len(lines)):

		#ignore empty lines and comments
		if(lines[i]=="\n" or
				lines[i][0] == "#"):
			i += 1
			continue

		#remove newline at the end of the lines
		pathlist.update({lines[i][:-1]:lines[i+1][:-1]})

		i = i+2
	
	return pathlist
