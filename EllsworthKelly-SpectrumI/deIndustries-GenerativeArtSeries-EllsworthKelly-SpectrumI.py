#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-EllsworthKelly-SpectrumI
# deIndustries // Procedural Art Generation // Ellsworth Kelly - Spectrum I
# python code to procedurally generate Ellsworth Kelly - Spectrum I ref sfmoma
#
# 2016-02-14 v1.0
#
# pre-reqs: PIL

#Notes
#Each colour is denoted in hex triplet: #xxxxxx [sRGB]

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-EllsworthKelly-SpectrumI"
print (title + " " + str(now))
print '-----------------------------------------'

#COLOUR
#-------------
spectrumA = "#edd54d"
spectrumB = "#66ba4b"
spectrumC = "#01a046"
spectrumD = "#018877"
spectrumE = "#016fae"
spectrumF = "#315ab6"
spectrumG = "#72448f"
spectrumH = "#97476c"
spectrumI = "#b63752"
spectrumJ = "#e03434"
spectrumK = "#f54e2a"
spectrumL = "#ff752a"
spectrumM = "#feaf14"
spectrumN = "#fde058"
spectrumColours = (spectrumA,spectrumB,spectrumC,spectrumD,spectrumE,spectrumF,spectrumG,spectrumH,spectrumI,spectrumJ,spectrumK,spectrumL,spectrumM,spectrumN)

#IMAGE RENDERING
#-------------

#Image Dimensions
xDimension=4096 #x pixels. ydimension controlled by number of rows (see below)
yratio=1.0     #x:y ratio, >1 makes y>x (portrait)
yDimension=int(math.ceil(xDimension*yratio))  #Automatic  height ref correct ratio #also needs to be int, not float

#Artwork Specific Ratios
rows    = 1
columns = 14

#Artwork Colours
colourArray = spectrumColours

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension))
dr = ImageDraw.Draw(im)

#Create Boxes
xWidth = xDimension/columns
xSpacer = 0 #these are zero to keep generation code similar to other projects
ySpacer = 0
yOrigin = 0

for c in range(0, columns): #0 to columns
    xOrigin = xWidth*c
    dr.rectangle(( (xOrigin+xSpacer,yOrigin+ySpacer),(xOrigin+xWidth,yDimension) ), fill=colourArray[c])

#Complete File
#-------------
filename = title + str(now) + ".png"
im.save(filename)
print ("Wrote image to file: " + filename)
