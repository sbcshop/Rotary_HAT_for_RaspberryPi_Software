#!/usr/bin/python
import os
import sys 
import time
import spidev as SPI
sys.path.append("..")
from lib import Round_Touch
from PIL import Image,ImageDraw,ImageFont

TP_INT = 4  # touch interrupt pin define
Mode = 0
touch = Round_Touch.touch()
           
try:
    disp = Round_Touch.lcd()
    disp.Init()
    disp.clear()
    touch.init()
    def Callback(TP_INT):       
            touch.Gestures = touch.Touch_Read_Byte(0x01)
            
    touch.int_irq(Callback)
    touch.Set_Mode(Mode)
    image = Image.open('../pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)

    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    
    while True:              
                if touch.Gestures == 0x01:
                            image = Image.open('../pic/img1.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                            print("UP")

                elif touch.Gestures == 0x02:                                 
                            image = Image.open('../pic/img6.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                            print("DOWN")
                                    
                                    
                elif touch.Gestures == 0x03:
                            image = Image.open('../pic/img7.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                            print("LEFT")     
                      
                                    
                elif touch.Gestures == 0x04:
                            image = Image.open('../pic/img2.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                            print("RIGHT") 

                elif touch.Gestures == 0x0C:
                            image = Image.open('../pic/img4.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                            print("LONG PRESS") 
                      
                                    
                elif touch.Gestures == 0x0B:
                            image = Image.open('../pic/img8.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                            print("DOUBLE TAB") 
                            
except KeyboardInterrupt:
    disp.module_exit()
    exit()

