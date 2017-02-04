#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-EllsworthKelly-ColorsForALargeWall
# deIndustries // Procedural Art Generation // Ellsworth Kelly Colors For A Large Wall (1951) at sfmoma. https://www.sfmoma.org/artwork/99.345
# python code to procedurally generate Ellsworth Kelly ColorsForALargeWall.
#
# 2016-02-04 v1.0
#
# pre-reqs: PIL

#Notes
#Each colour is denoted in hex triplet: #xxxxxx [sRGB]

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-EllsworthKelly-ColorsForALargeWall"
print (title + " " + str(now))
print '-----------------------------------------'

#COLOURS
#-------------
#Pallete
ekRed = "#c31a17";
ekOrange = "#cd5115";
ekYellow = "#e5c70f";
ekLightGreen  = "#76a152";
ekDarkGreen = "#162625";
ekLightBlue = "#305aa6";
ekDarkBlue = "#162465";
ekPink = "#c64853";
ekLightPurple = "#7e4f97";
ekDarkPurple = "#271930";
ekWhite = "#eae7e2";
ekBrown = "#2a201e";
ekBlack = "#161618";
ekDarkRightCorner = "#11111d";

#Array
##yes, this is just a 64 item array. Left to Right. Top to bottom
colourArray = (
               ekBrown, ekWhite, ekLightPurple, ekWhite, ekBlack, ekOrange, ekWhite, ekLightBlue,
               ekWhite, ekDarkGreen, ekBlack, ekWhite, ekYellow, ekWhite, ekPink, ekBlack,
               ekBlack, ekWhite, ekWhite, ekDarkBlue, ekWhite, ekWhite, ekWhite, ekOrange,
               ekRed, ekWhite, ekLightBlue, ekWhite, ekLightGreen, ekBlack, ekDarkPurple, ekWhite,
               ekWhite, ekDarkPurple, ekBlack, ekWhite, ekWhite, ekRed, ekWhite, ekDarkBlue,
               ekDarkGreen, ekWhite, ekWhite, ekLightBlue, ekWhite, ekWhite, ekDarkGreen, ekBlack,
               ekWhite, ekPink, ekLightGreen, ekWhite, ekBlack, ekLightPurple, ekWhite, ekWhite,
               ekBlack, ekWhite, ekDarkPurple, ekYellow, ekWhite, ekBlack, ekPink, ekDarkRightCorner
               );


#IMAGE RENDERING
#-------------
#Image Dimensions
xDimension=2048 #x
yratio=1.00     #x:y ratio, >1 makes y>x
yDimension=int(math.ceil(xDimension*yratio))  #Automatic  height ref correct ratio #also needs to be int, not float

#Artwork Specific Ratios
rows    = 8;
columns = 8;

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), "#ffffff")
dr = ImageDraw.Draw(im)

#Draw Colours
panelwidth = xDimension/rows; #2048/8 = 256px
panelheight = yDimension/columns;

for r in range(0, rows): #0 to 8
    for c in range(0, columns): #0 to 8
        xOrigin = panelwidth*c;
        yOrigin = panelheight*r;
        dr.rectangle(( (xOrigin,yOrigin),(xOrigin+panelwidth,yOrigin+panelheight)), fill=colourArray[r*8+c],outline=1);
        #debugline print "row,column: " + str(r) + "," + str(c) + ", " + colourArray[r*8+c];

#Create Border
dr.rectangle(((0,0),(xDimension,yDimension)), outline=0) #full img border

#Complete File
#-------------
filename = title + str(now) + ".png"
im.save(filename)
print ("Wrote image to file: " + filename)
