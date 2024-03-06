''' Demo to test Display working '''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys 
import time
import spidev as SPI
sys.path.append("..")
from lib import Round_Touch
from PIL import Image,ImageDraw,ImageFont

from datetime import datetime

Font1 = ImageFont.truetype("../Font/Font02.ttf",45)
Font2 = ImageFont.truetype("../Font/Font02.ttf",20)


try:
    disp = Round_Touch.lcd()
    disp.Init()
    disp.clear()
    image = Image.open('../pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)
    while True:
        image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
        draw2 = ImageDraw.Draw(image2)
        now = datetime.now() # current date and time
        time1 = now.strftime("%H:%M:%S")
        date1 = now.strftime("%d/%m/%Y")

        draw2.arc((1,1,237,237),0, 360, fill =(26,246,136), width=9)
       
        draw2.text((55, 90), time1, font=Font1, fill = (255,255,255))
        draw2.text((75, 138), date1, font=Font2, fill = (255,255,255))
        im_r2=image2.rotate(0)
        disp.ShowImage(im_r2)
                
           
except KeyboardInterrupt:
    disp.module_exit()
    exit()
