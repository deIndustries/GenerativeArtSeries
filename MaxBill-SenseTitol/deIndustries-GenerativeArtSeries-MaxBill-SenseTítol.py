#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-MaxBill-Sense-titol
# deIndustries & bmd // Procedural Art Generation // Max Bill // Sense títol, 1979 // http://www.artnet.com/artists/max-bill/sense-t%C3%ADtol-a-8InGDUsrLIluZAfYWI-6w2
# python code to procedurally generate Max Bill Artwork

# 2019-01-04 v1.0
#
# pre-reqs: PIL
#
# Art Notes
# 65 x 50 cm. (25.6 x 19.7 in.) on paper. 
# 66 in the world!
# Actual Shape is symmetrical, built from little squares. 5x1, 3x1, 1x1, 1x2, 1x4, 1x6, 1x5, 1x3, 1x4, 1x1, 1x2
#
# Colour Notes
#  (0,0)       x 
#                                            
#            | |                                 
#          | | | |                               
#        | | | | | |                                
#       -| | | | | --                               
#      --- | | | -----                                
#     ------ | --------         y                            
#     -------- | ------                                   
#      ------| | -----                               
#        --- | | | --                             
#         -| | | | |                              
#          | | | |                               
#            | |                                                                            
#                           (x,y)
#
#
# Changelog
# v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
from matplotlib import colors                   #for rgb conversion.
 #colors.hex2color('#ffffff')                   #==> (1.0, 1.0, 1.0)
 #colors.rgb2hex((1.0, 1.0, 1.0))               #==> '#ffffff'
 #dr.rectangle(( (origin,origin),(origin+6*b,origin-b)), fill=colors.rgb2hex(maxbill2[1]), outline=Lines) #Orange6er
 #dr.polygon([(0,yDimension/2), (xDimension,0),(xDimension,yDimension/2)], fill = colors.rgb2hex(maxbill2[1])) 				# Magenta with 1/2 height
 #
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-MaxBill-SenseTitol"
print(title + " " + str(now))
print('-----------------------------------------')

#COLOURS & PANEL DIMENSIONS
#-------------  
#FORMAT    ("NAME", colour RGB)
maxbill0  = ("bg"  , ( 217.0/255, 211.0/255, 197.0/255))  #background
maxbill1  = ("r"   , ( 217.0/255,  12.0/255,   0.0/255))  
maxbill2  = ("o"   , ( 248.0/255,  50.0/255,   2.0/255))  
maxbill3  = ("y"   , ( 251.0/255, 131.0/255,   2.0/255))  
maxbill4  = ("lg"  , (  39.0/255, 154.0/255,  74.0/255))  
maxbill5  = ("dg"  , (  15.0/255,  87.0/255, 101.0/255))  
maxbill6  = ("b"   , (   0.0/255,  33.0/255, 193.0/255))    
maxbill7  = ("i"   , ( 175.0/255,   6.0/255,  55.0/255))  #lighter purple
maxbill8  = ("v"   , (  88.0/255,   1.0/255,  53.0/255))  

#IMAGE RENDERING
#-------------
#Image Dimensions
xDimension=1995 #3990                           			#x (1600px default) ideally divisibly by 0.07
yratio=1.0                                		   			#x:y ratio, >1 makes y>x. Original = 1.0
yDimension=int(math.ceil(xDimension*yratio))    			#Automatic  height ref correct ratio #also needs to be int, not float

# Design Principle: Square Image with Blue Background. 
# First overlayed triangle has 1/2 height
# Second overlayed triangle has 1/3 height

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), colors.rgb2hex(maxbill0[1]))
dr = ImageDraw.Draw(im)

#Calculations
origin = xDimension/2										# Centre Co-ordinate (origin,origin)
ratioOf6BlocksToPageWidth = 0.84/2 							# 0.42 from origin to end of 6er block
b = xDimension*ratioOf6BlocksToPageWidth/6		# Block Dimensions = 0.07*x precis

#Options
Lines=None #(change to 0 for tiny borders on pieces)

#Create Colours!
## 6er
dr.rectangle(( (origin,origin),(origin+6*b,origin-b)), fill=colors.rgb2hex(maxbill2[1]), outline=Lines) #Orange6er
dr.rectangle(( (origin,origin),(origin-6*b,origin+b)), fill=colors.rgb2hex(maxbill6[1]), outline=Lines) #Blue
dr.rectangle(( (origin,origin),(origin+b,origin+6*b)), fill=colors.rgb2hex(maxbill4[1]), outline=Lines) #LGreen
dr.rectangle(( (origin,origin),(origin-b,origin-6*b)), fill=colors.rgb2hex(maxbill7[1]), outline=Lines) #Purple

## 5er
dr.rectangle(( (origin+b,origin),(origin+6*b,origin+b)), fill=colors.rgb2hex(maxbill1[1]), outline=Lines) #Red
dr.rectangle(( (origin-b,origin),(origin-6*b,origin-b)), fill=colors.rgb2hex(maxbill5[1]), outline=Lines) #DG
dr.rectangle(( (origin,origin+b),(origin-b,origin+6*b)), fill=colors.rgb2hex(maxbill3[1]), outline=Lines) #Yello
dr.rectangle(( (origin,origin-b),(origin+b,origin-6*b)), fill=colors.rgb2hex(maxbill8[1]), outline=Lines) #DP

##4er
dr.rectangle(( (origin+b,origin+b),(origin+2*b,origin+5*b)), fill=colors.rgb2hex(maxbill5[1]), outline=Lines) #DG
dr.rectangle(( (origin-b,origin+b),(origin-5*b,origin+2*b)), fill=colors.rgb2hex(maxbill8[1]), outline=Lines) #DP
dr.rectangle(( (origin-b,origin-b),(origin-2*b,origin-5*b)), fill=colors.rgb2hex(maxbill1[1]), outline=Lines) #Red
dr.rectangle(( (origin+b,origin-b),(origin+5*b,origin-2*b)), fill=colors.rgb2hex(maxbill3[1]), outline=Lines) #Yellow

##3er
dr.rectangle(( (origin+2*b,origin+b),(origin+5*b,origin+2*b)), fill=colors.rgb2hex(maxbill7[1]), outline=Lines) #LP
dr.rectangle(( (origin-b,origin+2*b),(origin-2*b,origin+5*b)), fill=colors.rgb2hex(maxbill2[1]), outline=Lines) #Orange
dr.rectangle(( (origin-2*b,origin-b),(origin-5*b,origin-2*b)), fill=colors.rgb2hex(maxbill4[1]), outline=Lines) #LG
dr.rectangle(( (origin+b,origin-2*b),(origin+2*b,origin-5*b)), fill=colors.rgb2hex(maxbill6[1]), outline=Lines) #Blue

##2er
dr.rectangle(( (origin+2*b,origin+2*b),(origin+3*b,origin+4*b)), fill=colors.rgb2hex(maxbill6[1]), outline=Lines) #Blue
dr.rectangle(( (origin-2*b,origin+2*b),(origin-4*b,origin+3*b)), fill=colors.rgb2hex(maxbill7[1]), outline=Lines) #LP
dr.rectangle(( (origin-2*b,origin-2*b),(origin-3*b,origin-4*b)), fill=colors.rgb2hex(maxbill2[1]), outline=Lines) #Orange
dr.rectangle(( (origin+2*b,origin-2*b),(origin+4*b,origin-3*b)), fill=colors.rgb2hex(maxbill4[1]), outline=Lines) #LG

##1er
dr.rectangle(( (origin+3*b,origin+2*b),(origin+4*b,origin+3*b)), fill=colors.rgb2hex(maxbill8[1]), outline=Lines) #DP
dr.rectangle(( (origin-2*b,origin+3*b),(origin-3*b,origin+4*b)), fill=colors.rgb2hex(maxbill1[1]), outline=Lines) #Red
dr.rectangle(( (origin-3*b,origin-2*b),(origin-4*b,origin-3*b)), fill=colors.rgb2hex(maxbill3[1]), outline=Lines) #Ywllow 
dr.rectangle(( (origin+2*b,origin-3*b),(origin+3*b,origin-4*b)), fill=colors.rgb2hex(maxbill5[1]), outline=Lines) #DG

#Complete File
filename = title + "_" + str(now) + ".png"
im.save(filename)
print("Wrote image to file: " + filename)
