#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-EllsworthKelly-ChathamSeries
# deIndustries // Procedural Art Generation // Ellsworth Kelly Chatham Series (1971) at MOMA NYC. Collection of 14.
# python code to procedurally generate Ellsworth Kelly Chatham Series.
# Reference: https://ellsworthkelly.org/exhibition/ellsworth-kelly-chatham-series/ and http://press.moma.org/wp-content/files_mf/ellsworthkellychathamserieschecklistwithphotocredits.pdf
#
# 2018-06-11 v1.0
#
# pre-reqs: PIL

# Colour Notes
# 2 Panels (A&B), each a different colour [R,G,B]. Two panels defined each by a single ratio.
# 
#      |------------------|           ▲
#      |        A         |  topPanelHeight [0-1]
#      |                  |         
#      |------------------|           ▼
#      |      |   
#      |      |   
#      |      |  
#      |  B   |  
#      |      |  
#      |      | 
#      |      | 
#      |------| 
#
#      ◀      ▶  bottomPanelWidth [0-1]

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
from matplotlib import colors                   #for rgb conversion.
 #colors.hex2color('#ffffff')                   #==> (1.0, 1.0, 1.0)
 #colors.rgb2hex((1.0, 1.0, 1.0))               #==> '#ffffff'
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-EllsworthKelly-ChathamSeries"
print(title + " " + str(now))
print('-----------------------------------------')

#COLOURS & PANEL DIMENSIONS
#-------------  
#FORMAT    ("NAME",topPanelHeight,bottomPanelWidth, colour 1 RGB, colour 2 RGB)
chatham1  = ("Chatham I"   , 0.39 , 0.310, ( 245.0/255, 243.0/255, 230.0/255), (   5.0/255,   5.0/255,   8.0/255))  #Chatham I     White Black
chatham2  = ("Chatham II"  , 0.336, 0.377, (  26.0/255, 121.0/255, 194.0/255), ( 226.0/255,  59.0/255,  32.0/255))  #Chatham II    Blue Red
chatham3  = ("Chatham III" , 0.371, 0.290, (  12.0/255,  18.0/255,  15.0/255), (  47.0/255,  92.0/255, 138.0/255))  #Chatham III   Black Blue
chatham4  = ("Chatham IV"  , 0.385, 0.430, (  16.0/255,  59.0/255, 124.0/255), ( 204.0/255,  33.0/255,  37.0/255))  #Chatham IV    BLue Red-Orange
chatham5  = ("Chatham V"   , 0.422, 0.460, ( 209.0/255,  35.0/255,  51.0/255), (  22.0/255, 100.0/255, 146.0/255))  #Chatham V     Red Blue
chatham6  = ("Chatham VI"  , 0.273, 0.295, ( 209.0/255,  35.0/255,  51.0/255), (  22.0/255, 100.0/255, 146.0/255))  #Chatham VI    Red Blue
chatham7  = ("Chatham VII" , 0.361 ,0.418, (  12.0/255,  18.0/255,  15.0/255), ( 245.0/255, 243.0/255, 230.0/255))  #Chatham VII   Black White
chatham8  = ("Chatham VIII", 0.321, 0.355, ( 209.0/255,  35.0/255,  51.0/255), ( 241.0/255, 226.0/255,  10.0/255))  #Chatham VIII  Red Yellow
chatham9  = ("Chatham IX"  , 0.370, 0.424, (  12.0/255,  18.0/255,  15.0/255), (  42.0/255, 166.0/255,  79.0/255))  #Chatham IX    Black Green
chatham10 = ("Chatham X"   , 0.370, 0.415, (  12.0/255,  18.0/255,  15.0/255), ( 209.0/255,  35.0/255,  51.0/255))  #Chatham X     Black Red
chatham11 = ("Chatham XI"  , 0.373, 0.474, (  12.0/255,  36.0/255, 105.0/255), ( 247.0/255, 207.0/255,  75.0/255))  #Chatham XI    Blue Yellow
chatham12 = ("Chatham XII" , 0.514, 0.547, ( 241.0/255, 226.0/255,  10.0/255), (  12.0/255,  18.0/255,  15.0/255))  #Chatham XII   Yellow Black
chatham13 = ("Chatham XIII", 0.482, 0.566, ( 241.0/255, 226.0/255,  10.0/255), ( 209.0/255,  35.0/255,  51.0/255))  #Chatham XIII  Yellow Red
chatham14 = ("Chatham XIV" , 0.489, 0.522, (  12.0/255,  18.0/255,  15.0/255), ( 245.0/255, 243.0/255, 230.0/255))  #Chatham XIV   Black White

selectedpiece = chatham1                        #change this to select a format

topPanelHeight = selectedpiece[1]
bottomPanelWidth = selectedpiece[2]
rgb = (colors.rgb2hex(selectedpiece[3]),colors.rgb2hex(selectedpiece[4]))
print(rgb)

#IMAGE RENDERING
#-------------
#Image Dimensions
xDimension=1600                                 #x
yratio=1.13                                     #x:y ratio, >1 makes y>x
yDimension=int(math.ceil(xDimension*yratio))    #Automatic  height ref correct ratio #also needs to be int, not float

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), "#ffffff")
dr = ImageDraw.Draw(im)

#Create Colour Panels (Origin = Top Left of Canvas)
dr.rectangle(( (0,0), (yDimension,yDimension*topPanelHeight)), fill=rgb[0],outline=0)
dr.rectangle(( (0,yDimension*topPanelHeight), (bottomPanelWidth*xDimension,yDimension)), fill=rgb[1],outline=0)

#Complete File
filename = title + "_" + selectedpiece[0] + "_" + str(now) + ".png"
im.save(filename)
print("Wrote image to file: " + filename)
