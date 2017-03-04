#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-BlinkyPalermo-Triptychon
# deIndustries // Procedural Art Generation // Blinky Palermo Triptychon (1972)
# python code to procedurally generate Blinky Palermo Triptychon.
#
# 2016-02-12 v1.0
#
# pre-reqs: PIL

#Notes
#Each colour is denoted in hex triplet: #xxxxxx [sRGB]

#Changelog
#- v1.0 orig release

# PALERMO PANEL STYLE3 (P3)
# The 4 Panels is created from the following array (A,B,C,D,E,F,G,H,I) where:
#        s
#      |----------------------------|        |----------------------------|        |----------------------------|
#   s  |                            |        |                            |        |                            |
#      |             A              |        |              D             |        |              G             |
#      |                            |        |                            |        |                            |
#      |----------------------------|        |----------------------------|        |----------------------------|
#      |                            |        |                            |        |                            |
#      |             B              |        |              E             |        |              H             |
#      |                            |        |                            |        |                            |
#      |----------------------------|        |----------------------------|        |----------------------------|
#      |                            |        |                            |        |                            |
#      |             C              |        |              F             |        |              I             |
#      |                            |        |                            |        |                            |
#      |----------------------------|        |----------------------------|        |----------------------------|

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-BlinkyPalermo-Triptychon"
print (title + " " + str(now))
print '-----------------------------------------'

#COLOUR
#-------------

triptychonDarkRed   = "#8f1719"
triptychonLightRed  = "#c11128"
triptychonBlack     = "#131112"
triptychonBrown     = "#be9a76"
triptychonGrey      = "#463942"
triptychonDarkBlue  = "#1a182e"
triptychonLightBlue = "#121f4b"
triptychonColours   = (triptychonLightRed,triptychonDarkRed,triptychonBlack,triptychonBrown,triptychonGrey,triptychonBlack,triptychonLightBlue,triptychonDarkBlue,triptychonBlack);
triptychonRatio = (0.276, 0.378, 0.346)
triptychon = ('P3',triptychonRatio, triptychonColours)

#IMAGE RENDERING
#-------------

#Define Image Dimensions
xDimension = 800 #panel width
yratio=1.00     #x:y ratio, >1 makes y>x
yDimension = int(math.ceil(xDimension*yratio))  #Automatic Panel height ref correct ratio #also needs to be int, not float
#smallyDimension = int(0.333*yDimension) #top and bottom colours of each panel i.e. 13% of height per stripe. no border
xSpace = xDimension/16 #space around panels
ySpace = xSpace

#Define Format
painting = triptychon
colourStyle = painting[0]
colourRatio = painting[1]
colourArray = painting[2]

#Create Canvas
im = Image.new('RGB', (xDimension*3+xSpace*2,yDimension), (255,255,255)) #has internal spaces only
dr = ImageDraw.Draw(im)

#Create Colours
if colourStyle == "P3":
    panels=3 #number of panels
    for p in range(0, panels):
        xOrigin = xDimension*p + xSpace*(p)
        dr.rectangle(((xOrigin,0),(xOrigin+xDimension,yDimension*colourRatio[0])), fill=colourArray[3*p])                            #Main Panel BG   #colour= 0,3,6,9
        dr.rectangle(((xOrigin,yDimension*colourRatio[0]),(xOrigin+xDimension,yDimension*(colourRatio[0]+colourRatio[1]))), fill=colourArray[3*p+1])                     #Top Colour      #colour= 1,4,7,10
        dr.rectangle(((xOrigin,yDimension*(colourRatio[0]+colourRatio[1])),(xOrigin+xDimension,yDimension)), fill=colourArray[3*p+2]) #Bottom Colour   #colour= 2,5,8,11

#Complete File
#-------------
filename = title + str(now) + ".png"
imWithEdgeSpaces = Image.new('RGB', (xDimension*3+xSpace*4,yDimension+ySpace*2), (255,255,255)) #has internal spaces only
imWithEdgeSpaces.paste(im,(xSpace,ySpace))
imWithEdgeSpaces.save(filename) #img with spaces on each edge

print ("Wrote image to file: " + filename)
