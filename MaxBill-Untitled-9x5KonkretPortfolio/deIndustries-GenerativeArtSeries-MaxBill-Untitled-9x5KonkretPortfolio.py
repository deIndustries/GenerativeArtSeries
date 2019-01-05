#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-MaxBill-Untitled
# deIndustries & bmd // Procedural Art Generation // Max Bill // Untitled from 9x5 Konkret Portfolio 1973 // https://www.artsy.net/artwork/max-bill-untitled-from-9x5-konkret-portfolio
# python code to procedurally generate Max Bill Artwork

# 2018-12-27 v1.0
#
# pre-reqs: PIL

# Colour Notes
#  (0,0)      x 
#    _____________________
#	 |			        /| Top at 1/2 y
#    |               /	 |
#    |            / 	 |
#    |         /         |  
#    |      /          # | Top at 1/3 y
#    |   /        #      |
#    |/   #              |
#    _____________________                  y
#	 |			   #    /| Mirrored Below.
#    |        #       /	 |
#    |  #          /  	 |
#    |          /        | 
#    |      /            |
#    |   /               |
#    |/                  |
#    _____________________ (x,y)
#
#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
from matplotlib import colors                   #for rgb conversion.
 #colors.hex2color('#ffffff')                   #==> (1.0, 1.0, 1.0)
 #colors.rgb2hex((1.0, 1.0, 1.0))               #==> '#ffffff'
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-MaxBill-UntitledFrom9x5Konkret"
print(title + " " + str(now))
print('-----------------------------------------')

#COLOURS & PANEL DIMENSIONS
#-------------  
#FORMAT    ("NAME", colour RGB)
maxbill1  = ("Blue"      , (  40.0/255, 131.0/255, 196.0/255))  
maxbill2  = ("Magenta"   , ( 168.0/255,  50.0/255, 125.0/255))  
maxbill3  = ("Red"       , ( 211.0/255,  24.0/255,  23.0/255))  
maxbill4  = ("Turquoise" , ( 250.0/255, 113.0/255,  18.0/255))  
maxbill5  = ("Green"     , (  75.0/255, 208.0/255, 126.0/255))  

#IMAGE RENDERING
#-------------
#Image Dimensions
xDimension=4000                                 #x (1600px default)
yratio=1.0                                		#x:y ratio, >1 makes y>x. Original = 1.0
yDimension=int(math.ceil(xDimension*yratio))    #Automatic  height ref correct ratio #also needs to be int, not float

# Design Principle: Square Image with Blue Background. 
# First overlayed triangle has 1/2 height
# Second overlayed triangle has 1/3 height

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), colors.rgb2hex(maxbill1[1]))
dr = ImageDraw.Draw(im)

#Create Colours!

#Top Half
dr.polygon([(0,yDimension/2), (xDimension,0),(xDimension,yDimension/2)], fill = colors.rgb2hex(maxbill2[1])) 				# Magenta with 1/2 height
dr.polygon([(0,yDimension/2), (xDimension, yDimension/3),(xDimension,yDimension/2)], fill = colors.rgb2hex(maxbill3[1])) 	# Red with 1/3 height

#Bottom Half
dr.polygon([(0,yDimension/2), (0,yDimension),(xDimension,yDimension/2)], fill = colors.rgb2hex(maxbill5[1])) 				# Turquoise with 1/2 height
dr.polygon([(0,yDimension/2), (0,yDimension*2/3),(xDimension,yDimension/2)], fill = colors.rgb2hex(maxbill4[1])) 			# Orange with -1/3 height

#Complete File
filename = title + "_" + str(now) + ".png"
im.save(filename)
print("Wrote image to file: " + filename)
