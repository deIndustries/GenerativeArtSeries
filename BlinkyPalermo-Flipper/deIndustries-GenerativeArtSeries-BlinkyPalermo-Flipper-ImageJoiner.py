#!/usr/bin/python
# coding: utf-8

# deIndustries-GenerativeArtSeries-BlinkyPalermo-Flipper-JoinerTool
# deIndustries // Procedural Art Generation // Blinky Palermo Flipper (1970)
# python code to procedurally generate Blinky Palermo Triptychon ref https://www.moma.org/collection/works/62216
#
# 2016-02-12 v1.0
#
# pre-reqs: PIL

#Changelog
#- v1.0 orig release

from PIL import Image, ImageFont, ImageDraw
import math, time
now = int(time.time())

title = "deIndustries-GenerativeArtSeries-BlinkyPalermo-Flipper-JoinerTool"
print (title + " " + str(now))
print '-----------------------------------------'
filename = title + str(now) + ".png"

#COLOUR
#-------------
flipperWhite        = "#eeeeee"
spaceBetweenImages = 200

#Create Canvas
images = map(Image.open, ['deIndustries-GenerativeArtSeries-BlinkyPalermo-Flipper-SpacerNone.png', 'deIndustries-GenerativeArtSeries-BlinkyPalermo-Flipper-Spacer.png'])
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)+spaceBetweenImages
max_height = max(heights)

im3 = Image.new('RGB', (total_width, max_height), flipperWhite)
x_offset = 0
for im in images:
  im3.paste(im, (x_offset,0))
  x_offset += im.size[0]+spaceBetweenImages

#Complete File
#-------------
im3.save(filename)
print ("Wrote image to file: " + filename)
