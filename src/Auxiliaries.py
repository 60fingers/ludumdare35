import pygame, os

def readImagePathList(self):
	paths = open("paths.txt","r")
	pathlist = {}
	lines = []
	#read all lines from the file
	for line in paths:
		line.append(line)
		
	paths.close()
	
	#write lines in the dictionary
	i = 0
	while i < len(lines)
		pathlist.update({lines[i]:lines[i+1]})
		i = i+2
	
	return pathlist
