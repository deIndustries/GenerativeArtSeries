#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-BlinkyPalermo-Flipper
# deIndustries // Procedural Art Generation // Blinky Palermo Flipper (1970)
# python code to procedurally generate Blinky Palermo Triptychon ref https://www.moma.org/collection/works/62216
#
# 2016-02-12 v1.0
#
# pre-reqs: PIL

#Notes
#Each colour is denoted in hex triplet: #xxxxxx [sRGB]

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-BlinkyPalermo-Flipper"
print (title + " " + str(now))
print '-----------------------------------------'

#COLOUR
#-------------
flipperRed          = "#d44f40"
flipperWhite        = "#eeeeee"
flipperBlue         = "#4560cb" #bg colour
flipperColours      = (flipperRed, flipperWhite, flipperBlue)
flipperColours2      = (flipperRed, flipperWhite, flipperWhite)

#IMAGE RENDERING
#-------------
#Implementation Notes, this is designed with the background as blue, and the white/red squares are drawn on top

#Image Dimensions
xDimension=2048 #x. ydimension controlled by number of rows (see below)

#Artwork Specific Ratios
rows    = 6
columns = 5
spacerRatio = 0.12 #Ratio of Square Dimension to Spacer
colourSwitch = 0 # 0/1 to allow for colour alternation
squareDimension = xDimension/(columns+spacerRatio) #has an extra spacer for correct display
spacer = squareDimension*spacerRatio
yDimension=int(math.ceil(rows*squareDimension+spacer))

#Artwork Colours
colourArray = flipperColours2

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), colourArray[2])
dr = ImageDraw.Draw(im)

#Create Squares

print ("Creating Image with Rows " + str(rows) + " and Columns: " + str(columns))
xSpacer = spacer
ySpacer = spacer

for r in range(0, rows): #0 to 8
    for c in range(0, columns): #0 to 8
        xOrigin = squareDimension*c
        yOrigin = squareDimension*r
        dr.rectangle(( (xOrigin+xSpacer,yOrigin+ySpacer),(xOrigin+squareDimension,yOrigin+squareDimension) ), fill=colourArray[colourSwitch])
        if (colourSwitch==0):
            colourSwitch=1
        else:
            colourSwitch=0

#Complete File
#-------------
filename = title + str(now) + ".png"
im2 = im.crop((int(spacer), int(spacer), int(xDimension-spacer), int(yDimension-spacer))).save(filename)
print ("Wrote image to file: " + filename)
