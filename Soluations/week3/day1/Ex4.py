#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:13:43 2019

@author: rawabi
"""


#Ex-4:
from PIL import Image,ImageFilter
from PIL import ImageDraw
im=Image.open("cat.jpg")
im2=Image.open("cat2.jpg").resize(im.size)
im2.show()
#1
print(im.format, im.size, im.mode)
im.show()

imgflip=im.transpose(Image.FLIP_TOP_BOTTOM)
imgflip.show()

greyimage=im.convert('L')
greyimage.show()

crop=im.crop((0,0,50,50))
crop.show()

draw=ImageDraw.Draw(im)
draw.line((0,0)+im.size, fill=(255,255,255))
draw.line((0,im.size[1],im.size[0],0), fill=(255,255,255))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),'rawabi',fill=(225,225,0))
im.show()

new=im.filter(ImageFilter.SHARPEN)
new.show()
enh=im.filter(ImageFilter.EDGE_ENHANCE)
enh.show()
find=im.filter(ImageFilter.FIND_EDGES)
find.show()
smo=im.filter(ImageFilter.SMOOTH)
smo.show()

Image.blend(im,im2,0.5).save('new.jpg'.format(0.5))
new=Image.open('new.jpg')
new.show()

blu=im.filter(ImageFilter.BLUR)
blu.show()

size=(128,128)
im.thumbnail(size)
im.show()

imagerot=im.rotate(90)
imagerot.show()

mask=Image.open('mask2.jpg')
mask=mask.resize(im.size)
Image.composite(im,im2,mask).save('maskimg.jpg')
imagMask=Image.open('maskimg.jpg')
imagMask.show()