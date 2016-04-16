import pygame, os

def readImagePathList():
	paths = open("paths.txt","r")
	pathlist = {}
	
	lines = paths.readlines()
	paths.close()
	
	#write lines in the dictionary
	i = 0
	while (i < len(lines)):
		pathlist.update({lines[i]:lines[i+1]})
		i = i+2
	
	return pathlist
