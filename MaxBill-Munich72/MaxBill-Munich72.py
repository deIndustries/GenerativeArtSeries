#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-MaxBill-Munich72
# deIndustries // Procedural Art Generation // Max Bill // Munich Olympics Poster
# python code to procedurally generate Max Bill Munich Olympics Poster
# Reference: https://www.picturethiscollection.com/products/detail/G1645MunichOlympicGa/en/

# 2018-12-04 v1.0
#
# pre-reqs: PIL

# Colour Notes
# 2 Panels (A&B), each a different colour [R,G,B]. Two panels defined each by a single ratio.
#    ___________________
#    |  \          /   | 
#    |   \        /    |
#    |    \      /     |
#    |\    \    /     /|
#    | \    \  /     / |
#    |  \    \/     /  |
#    |   \   / \   /   |
#    |    \ /   \ /    |
#    |    / \   / \    |
#    |   /   \ /   \   |
#	 |  /    / \    \  |
#    | /    /   \    \ |
#    |/    /     \    \|
#    |    /       \    |
#    |   /         \   | 
#    |  /           \  |
#    | /_____________\ |

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
from matplotlib import colors                   #for rgb conversion.
 #colors.hex2color('#ffffff')                   #==> (1.0, 1.0, 1.0)
 #colors.rgb2hex((1.0, 1.0, 1.0))               #==> '#ffffff'
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-MaxBill-Munich72"
print(title + " " + str(now))
print('-----------------------------------------')

#COLOURS & PANEL DIMENSIONS
#-------------  
#FORMAT    ("NAME", colour RGB)
maxbill1  = ("Red"   , ( 171.0/255,  36.0/255,  69.0/255))  
maxbill2  = ("Orange", ( 206.0/255,  61.0/255,  14.0/255))  
maxbill3  = ("Yellow", ( 204.0/255, 118.0/255,   0.0/255))  
maxbill4  = ("GreenL", (  47.0/255, 177.0/255,  71.0/255))  
maxbill5  = ("GreenD", (  34.0/255, 140.0/255,  95.0/255))  
maxbill6  = ("BlueL" , (  18.0/255, 115.0/255, 192.0/255))  
maxbill7  = ("BlueD" , (  34.0/255,  70.0/255, 158.0/255))  
maxbill8  = ("Purple", ( 130.0/255,  43.0/255, 128.0/255))  
maxbill9  = ("White" , ( 215.0/255, 215.0/255, 217.0/255))  

#IMAGE RENDERING
#-------------
#Image Dimensions
xDimension=1600                                 #x
yratio=1.37                                     #x:y ratio, >1 makes y>x
yDimension=int(math.ceil(xDimension*yratio))    #Automatic  height ref correct ratio #also needs to be int, not float

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), colors.rgb2hex(maxbill9[1]))
dr = ImageDraw.Draw(im)

#Create Colour Panels (Origin = Top Left of Canvas)

#Purple
dr.polygon([(0,0), (0,xDimension), (xDimension,0)], fill = colors.rgb2hex(maxbill8[1]))

#LightBLue
dr.polygon([(0,0), (xDimension,0), (xDimension,xDimension)], fill = colors.rgb2hex(maxbill6[1]))

#Dark BLue
dr.polygon([(0,0), (xDimension, 0), (xDimension*0.5,1*0.5*xDimension)], fill = colors.rgb2hex(maxbill7[1]))

#Light Green
dr.polygon([(0,yDimension), (xDimension,yDimension-xDimension), (xDimension,yDimension)], fill = colors.rgb2hex(maxbill4[1]))

#Orange
dr.polygon([(0,yDimension), (0,yDimension-xDimension), (xDimension,yDimension)], fill = colors.rgb2hex(maxbill2[1]))

#Bottom Yellow
dr.polygon([(0,yDimension), (xDimension, yDimension), (xDimension*0.5,yDimension-0.5*xDimension)], fill = colors.rgb2hex(maxbill3[1]))

#Dark Green
dr.polygon([(xDimension,xDimension), (xDimension,yDimension-xDimension), (yDimension*0.5,yDimension*0.5)], fill = colors.rgb2hex(maxbill5[1]))

#Red
dr.polygon([(0,xDimension), (0,yDimension-xDimension), (xDimension-yDimension/2,yDimension*0.5)], fill = colors.rgb2hex(maxbill1[1]))

#Complete File
filename = title + "_" + str(now) + ".png"
im.save(filename)
print("Wrote image to file: " + filename)
