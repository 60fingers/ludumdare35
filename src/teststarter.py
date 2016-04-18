import os, pygame


import MainControl

m = MainControl.MainControl()

o = m.world.objSurr_H_static((50,500),4)
for i in o:
	print(i.position)

input()


#m.main()
