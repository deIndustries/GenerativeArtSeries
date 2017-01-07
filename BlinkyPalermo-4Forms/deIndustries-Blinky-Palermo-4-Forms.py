#!/usr/bin/python
# coding: utf-8

# deIndustries-Blinky-Palermo-4-Forms
# deIndustries // Procedural Art Generation // Palermo To the People of New York City
# python code to procedurally generate Blink Palermo Style Images from the collection To the People of New York City.
#
# 2016-01-01 v1.2
#
# pre-reqs: PIL

#Code Notes
# based on stuff from: https://github.com/daviddoria/Examples/tree/master/Python/PIL
# and http://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html

#Art Notes
#Original Inspiration is Palermo - "To the People of New York" Collection.
#Namely Coney Island II
#Each Panel is (56.8 x 52 cm), i.e. 1.092 ratio.

#Colour Notes
#4 Panels, each panel with 2 colours (top/bottom sections are always the same)
#Each colour is denoted in [R,G,B] Where R/G/B is in range from 0-255

#Changelog v1.2
#-added second panel type P2, needing new array picture=(style,colourArray)

# PALERMO PANEL STYLE1 (P1)
# The 4 Panels is created from the following array of 8 tuples (A,B,C,D,E,F,G,H) where:
#               s
#      |------------------|      |------------------|      |------------------|      |------------------|
#   s  |         B        |      |         D        |      |         F        |      |         H        |
#      |------------------|      |------------------|      |------------------|      |------------------|
#      |                  |      |                  |      |                  |      |                  |
#      |                  |      |                  |      |                  |      |                  |
#      |         A        |      |         C        |      |         E        |      |         G        |
#      |                  |      |                  |      |                  |      |                  |
#      |                  |      |                  |      |                  |      |                  |
#      |------------------|      |------------------|      |------------------|      |------------------|
#      |         B        |      |         D        |      |         F        |      |         H        |
#      |------------------|      |------------------|      |------------------|      |------------------|
#

# PALERMO PANEL STYLE2 (P2)
# The 4 Panels is created from the following array of 12 tuples (A,B1,B2,C,D1,D2,E,F1,F2,G,H1,H2) where:
#               s
#      |------------------|      |------------------|      |------------------|      |------------------|
#   s  |         B1       |      |         D1       |      |        F1        |      |        H1        |
#      |------------------|      |------------------|      |------------------|      |------------------|
#      |                  |      |                  |      |                  |      |                  |
#      |                  |      |                  |      |                  |      |                  |
#      |         A        |      |         C        |      |         E        |      |         G        |
#      |                  |      |                  |      |                  |      |                  |
#      |                  |      |                  |      |                  |      |                  |
#      |------------------|      |------------------|      |------------------|      |------------------|
#      |         B2       |      |        D2        |      |        F2        |      |        H2        |
#      |------------------|      |------------------|      |------------------|      |------------------|
#


from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

print ("deIndustries-to-the-people-of-new-york-city" + str(now))
print '-----------------------------------------'

#COLOUR GROUPS
#-------------

#To The People of New York City Colours Exhibition (1976)
tpnycRed    = (206,36, 49)
tpnycYellow = (249, 172, 54)
tpnycBlack  = (0, 0, 0)
#coloursToThePeopleOfNYC_I    #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_II   #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_III  #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_IV   #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_V    #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_VI   #Shape Not Yet Implemented
coloursToThePeopleOfNYC_VII  =  ('P1', (tpnycRed,tpnycYellow,tpnycRed,tpnycBlack,tpnycYellow,tpnycRed,tpnycBlack,tpnycRed))
coloursToThePeopleOfNYC_VIII =  ('P1', (tpnycYellow,tpnycRed,tpnycYellow,tpnycBlack,tpnycRed,tpnycYellow,tpnycBlack,tpnycYellow))
coloursToThePeopleOfNYC_IX   =  ('P1', (tpnycRed,tpnycYellow,tpnycYellow,tpnycRed,tpnycRed,tpnycBlack,tpnycBlack,tpnycRed))
coloursToThePeopleOfNYC_X    =  ('P1', (tpnycYellow,tpnycRed,tpnycRed,tpnycYellow,tpnycYellow,tpnycBlack,tpnycBlack,tpnycYellow))
#coloursToThePeopleOfNYC_XI    #Shape Not Yet Implemented
#coloursToThePeopleOfNYC_XII   #Shape Not Yet Implemented

#Coney Island II (1975)
coloursConeyIslandII =  ('P1', ( (32, 146, 138), (136, 58, 48), (208, 83, 51), (232, 209, 105), (27, 35, 116), (222, 142, 153), (30, 57, 52),  (212, 136, 40) ))


#Times of the Day Series (1975)
#Colours generally from dia NY, however timesOfTheDay_III taken from flickr (and not colour correct)
ttIIIOrange   = (206, 103,  26)
ttIIIYellow   = (190, 178,  56)
ttIIIAqua     = ( 12,  98,  97)
ttIIIWhite    = (214, 217, 222)
ttIIIDRed     = (160,  23,  30)
ttIIILRed     = (201,  47,  45)
ttIIIBrown    = ( 79,  41,  40)
ttIIIBlack    = ( 35,  35,  39)
ttdIVBrown   = (191,  86,  41)
ttdIVWhite   = (237, 241, 240)
ttdIVGrey    = (52,   52,  60)
ttdVWhite    = (237, 241, 240)
ttdVLGrey    = (210, 210, 210)
ttdVDGrey    = ( 56,  54,  59)
ttdVGreen    = (119, 198,  81)
ttdVOrange   = (194,  94,  42)
ttdVIRed     = (182,  70,  50)
ttdVIYellow  = (230,  217,  1)
ttdVIBlue    = ( 50,   80, 163)
timesOfTheDay_I    =  ('P1', ( (185,  55,  39), (168, 201, 216), (120, 174,  63), (167,  76,  29), (49, 123,  72), (201, 178,  76), ( 65,  33,  44),  ( 34,  33,  38) ))
timesOfTheDay_II   =  ('P1', ( (182, 181, 179), (194, 203, 208), (218, 160,   0), (218, 216, 217), (43,  89, 148), (157, 203, 219), ( 44,  43,  49),  (160,  86,  41) ))
timesOfTheDay_III  =  ('P1', ( ttIIIOrange,ttIIIYellow,ttIIIAqua,ttIIIWhite,ttIIIDRed,ttIIILRed,ttIIIBrown,ttIIIBlack ))
timesOfTheDay_IV  =  ('P1', (ttdIVWhite,ttdIVBrown,ttdIVBrown,ttdIVWhite,ttdIVBrown,ttdIVGrey,ttdIVGrey,ttdIVBrown))
timesOfTheDay_V   =  ('P1', (ttdVWhite,ttdVLGrey,ttdVGreen,ttdVOrange,ttdVOrange,ttdVGreen,ttdVDGrey,ttdVLGrey))
timesOfTheDay_VI  =  ('P1', (ttdVIRed,ttdVIYellow,ttdVIRed,ttdVIBlue,ttdVIBlue,ttdVIRed,ttdVIBlue,ttdVIYellow))

#4 White Forms (1975)
fWfWhite   = (232 , 235, 228)
fWfLBlue   = ( 60 , 110, 135)
fWfDBlue   = ( 36 ,  76, 105)
fWfLRed    = (172,  86, 84)
fWfDRed    = (155 , 95, 93)
fWf =  ('P1', (fWfWhite,fWfLBlue,fWfWhite,fWfLRed,fWfWhite,fWfDRed,fWfWhite,fWfDBlue))

#Return (1975)
returnMGreen = (0,59,30) #M ist für München
returnMRed = (180,0,12)
returnMBrightRed = (210,12,19)
returnMBlack = (1,1,1)
returnMYellow = (232,183,62)
returnMOrange =  (253,117,41)
returnMDarkBlue = (1, 1,30)
returnMBlue = (0,49,96)
returnM = ('P2', (returnMGreen,returnMRed,returnMRed,returnMBlack,returnMYellow,returnMBrightRed,returnMDarkBlue,returnMOrange,returnMOrange,returnMRed,returnMBlue,returnMBlue))

#IMAGE RENDERING
#-------------

#Define Image Dimensions
xDimension=400 #panel width
yDimension=int(math.ceil(xDimension*1.092))  #Automatic Panel height ref correct ratio #also needs to be int, not float
smallyDimension = int(0.13*yDimension) #top and bottom colours of each panel i.e. 13% of height per stripe. no border
xSpace=100 #space around panels
ySpace=100

#Select Painting to Draw
painting = timesOfTheDay_III     #v1.1 default option: coloursConeyIslandII

#Parse Out Format & Colours from Painting Array
colourStyle = painting[0]   #v1.2 new: Get Painting Format
colourArray = painting[1]   #v1.2 new: Get Painting Colours

#Create Canvas
im = Image.new('RGB', (xDimension*4+xSpace*3,yDimension), (255,255,255)) #has internal spaces only
dr = ImageDraw.Draw(im)

#Create Colours
if colourStyle == "P1":
    print "Palermo Style P1, With 8 Colours" #4 Panels in a Horizontal row (Palermo Style P1)
    panels=4 #number of panels
    for p in range(0, panels):
        xOrigin = xDimension*p + xSpace*(p)
        dr.rectangle(((xOrigin,0),(xOrigin+xDimension,yDimension)), fill=colourArray[2*p])                          #colour= 0,2,4,6
        dr.rectangle(((xOrigin,0),(xOrigin+xDimension,smallyDimension)), fill=colourArray[2*p+1])                   #colour= 1,3,5,7
        dr.rectangle(((xOrigin,yDimension-smallyDimension),(xOrigin+xDimension,yDimension)), fill=colourArray[2*p+1])

elif colourStyle == "P2":
    print "Palermo Style P2, With 12 Colours" #4 Panels in a Horizontal row (Palermo Style P2)
    panels=4 #number of panels
    for p in range(0, panels):
        print colourArray
        xOrigin = xDimension*p + xSpace*(p)
        dr.rectangle(((xOrigin,0),(xOrigin+xDimension,yDimension)), fill=colourArray[3*p])                            #Main Panel BG   #colour= 0,3,6,9
        dr.rectangle(((xOrigin,0),(xOrigin+xDimension,smallyDimension)), fill=colourArray[3*p+1])                     #Top Colour      #colour= 1,4,7,10
        dr.rectangle(((xOrigin,yDimension-smallyDimension),(xOrigin+xDimension,yDimension)), fill=colourArray[3*p+2]) #Bottom Colour   #colour= 2,5,8,11


#Complete File
#-------------
filename = "deIndustries - toThePeopleOfNewYorkCity" + str(now) + ".png"
#filename = "deIndustries - timesOfTheDay" + str(now) + ".png"
imWithEdgeSpaces = Image.new('RGB', (xDimension*4+xSpace*5,yDimension+ySpace*2), (255,255,255)) #has internal spaces only
imWithEdgeSpaces.paste(im,(xSpace,ySpace))
imWithEdgeSpaces.save(filename) #img with spaces on each edge

print ("Wrote image to file: " + filename)
#xdg-open "rectangle.png"
