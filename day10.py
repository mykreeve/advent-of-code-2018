#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os

filename="input/day10input.txt"
file=open(filename,"r")
points=[]
rates=[]
for line in file:
	x=""
	y=""
	velX=""
	velY=""
	for i in range(6):
		x=x+line[10+i]
		y=y+line[18+i]
	for i in range(2):
		velX=velX+line[36+i]
		velY=velY+line[40+i]
	points.append((int(x),int(y)))
	rates.append((int(velX),int(velY)))

def convert_x_value(x):
	lowX=float(125)
	highX=float(205)
	x=float((x-lowX)/float(highX-lowX))*130
	return int(x)

def convert_y_value(y):
	lowY=float(145)
	highY=float(195)
	y=float((y-lowY)/float(highY-lowY))*40
	return int(y)

def print_point(p):
	x=convert_x_value(p[0])
	y=convert_y_value(p[1])
	if x>=0 and x<131 and y>=0 and y<41:
		print("\033["+str(y)+";"+str(x)+"H*")

its=0
while True:
	print("\033[1;1H"+str(its))
	if its>10230:
		os.system('clear')
		print("\033[1;1H"+str(its))
		for p in points:
			print_point(p)
		entry=raw_input("")
	for p in range(len(points)):
		x=points[p][0]+rates[p][0]
		y=points[p][1]+rates[p][1]
		points[p]=(x,y)
	its+=1
