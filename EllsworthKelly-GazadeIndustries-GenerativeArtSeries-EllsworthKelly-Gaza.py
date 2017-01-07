#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-EllsworthKelly-Gaza
# deIndustries // Procedural Art Generation // Ellsworth Kelly Gaza (1956) at sfmoma. https://www.sfmoma.org/artwork/99.345
# python code to procedurally generate Ellsworth Kelly Gaza.
#
# 2016-01-07 v1.0
#
# pre-reqs: PIL

#Notes
#Each colour is denoted in hex triplet: #xxxxxx [sRGB]

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-EllsworthKelly-Gaza"
print (title + " " + str(now))
print '-----------------------------------------'

#COLOURS
#-------------
gazaColoursTuple= ("#fc4f02","#fed308","#ffb901","#fed001")

#IMAGE RENDERING
#-------------
#Image Dimensions
xDimension=1600 #x
yratio=1.13     #x:y ratio, >1 makes y>x
yDimension=int(math.ceil(xDimension*yratio))  #Automatic  height ref correct ratio #also needs to be int, not float
#Artwork Specific Ratios
##This is contribution of each vertical box as a % of total height (need to sum==1)
ratiosGaza = (0.14,0.14,0.27,0.45)

#Create Canvas
im = Image.new('RGB', (xDimension,yDimension), "#ffffff")
dr = ImageDraw.Draw(im)

#Create Colours
print "Ellsworth Kelly Gaza 1956"
dr.rectangle(((0,yDimension*ratiosGaza[0])                              ,(xDimension,yDimension*(ratiosGaza[0]+ratiosGaza[1])))                            ,fill=gazaColoursTuple[1]) #no outline due to both colours being on same canvas.
dr.rectangle(((0,0)                                                     ,(xDimension,yDimension*(ratiosGaza[0])))                                          ,fill=gazaColoursTuple[0])
dr.rectangle(((0,yDimension*(ratiosGaza[0]+ratiosGaza[1]))              ,(xDimension,yDimension*(ratiosGaza[0]+ratiosGaza[1]+ratiosGaza[2])))              ,fill=gazaColoursTuple[2],outline=0)
dr.rectangle(((0,yDimension*(ratiosGaza[0]+ratiosGaza[1]+ratiosGaza[2])),(xDimension,yDimension*(ratiosGaza[0]+ratiosGaza[1]+ratiosGaza[2]+ratiosGaza[3]))),fill=gazaColoursTuple[3],outline=0)
#Create Border
dr.rectangle(((0,0),(xDimension,yDimension)), outline=0) #full img border


#Complete File
#-------------
filename = title + str(now) + ".png"
im.save(filename)
print ("Wrote image to file: " + filename)
