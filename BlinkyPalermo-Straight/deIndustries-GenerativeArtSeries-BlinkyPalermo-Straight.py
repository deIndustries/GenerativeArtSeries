#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-BlinkyPalermo-Straight
# deIndustries // Procedural Art Generation // Blinky Palermo Straight (1965)
# python code to procedurally generate Blinky Palermo Straight from Book "Palermo Pinakothek Der Moderne München"

# 2016-02-14 v1.0
#
# pre-reqs: PIL

#Notes

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-BlinkyPalermo-Straight"
print (title + " " + str(now))
print '-----------------------------------------'

#COLOUR - Each colour is denoted in hex triplet: #xxxxxx [sRGB]
#-------------
straightBlue    = "#1244b3" #blue
straightYellow  = "#ffd505" #yellow
straightRed     = "#b82c09" #red
straightColours = (straightBlue, straightYellow, straightRed)

#IMAGE RENDERING
#-------------
#Implementation Notes, this is designed with a white background, vertical lines placed, then filled in with the smaller squares

#Art Notes
## columns aren't straight,
## colours aren't always in a set pattern,
## you can see pencil lines,
## i love it.

#Image Dimensions & Artwork Specific Ratios
xDimension  = 4096 #x pixels. ydimension controlled by number of rows (see below)
columns     = 26 #main coloured strips (default 13)
rows        = 34 #main coloured horizontal strips, consisting of little coloured sqares! (default 17)
yratio      = rows/columns    #x:y ratio, >1 makes y>x (portrait)
yDimension  = int(math.ceil(xDimension*yratio))  #Automatic  height ref correct ratio #also needs to be int, not float
squareDimension = math.ceil(xDimension/(columns*2)) # 2048/13/2 =78.76px

#Artwork Colours
colourArrayLines = straightColours


#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), "#ffffff")
dr = ImageDraw.Draw(im)

#Create Lines
print ("Creating Palermo Straight Artwork with Rows " + str(rows) + " and Columns: " + str(columns))
xSpacer = squareDimension
ySpacer = squareDimension
xOrigin = 0

print ("Drawing Columns")
for c in range(0, columns):
    if (c != 0): #no spacer on first column
        xOrigin = xOrigin + 2*xSpacer #add space between consecutive lines
    yOrigin = 0
    colourToDraw = colourArrayLines[c % 3] #select the right colour
    dr.rectangle(( (xOrigin,yOrigin),(xOrigin+squareDimension,yDimension) ), fill=colourToDraw)
    print ("Origin x,y: (" + str(xOrigin) + "," + str(yOrigin) + ") Destination x,y: (" + str(xOrigin+squareDimension) + "," + str(yDimension) + ") squareDimension: " + str(squareDimension) + ", colour: " + colourToDraw)

#Create Squares
print ("Drawing Squares")
xOrigin = 0 #reset x-cord to start
yOrigin = 0
for r in range(0, rows):
    for c in range(0, columns):
        xOrigin = squareDimension*(2*c)+xSpacer;
        yOrigin = squareDimension*(2*r);
        colourToDraw = colourArrayLines[(c+1+r%3)% 3] #select the right colour
        dr.rectangle(( (xOrigin,yOrigin),(xOrigin+squareDimension,yOrigin+squareDimension) ), fill=colourToDraw)
        print ("Origin x,y: (" + str(xOrigin) + "," + str(yOrigin) + ") Destination x,y: (" + str(xOrigin+squareDimension) + "," + str(yOrigin+squareDimension) + ") squareDimension: " + str(squareDimension) + ", colour: " + colourToDraw)

#Complete File
#-------------
filename = title + str(now) + ".png"
im.save(filename)
print ("Wrote image to file: " + filename)
