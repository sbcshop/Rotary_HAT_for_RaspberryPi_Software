#!/usr/bin/python
import os
import sys 
import time
import spidev as SPI
sys.path.append("..")
from lib import Round_Touch
from PIL import Image,ImageDraw,ImageFont

Font1 = ImageFont.truetype("../Font/Font00.ttf",25)
Font2 = ImageFont.truetype("../Font/Font02.ttf",20)

Mode = 1
touch = Round_Touch.touch()

try:
    disp = Round_Touch.lcd()
    disp.Init()
    disp.clear()
    touch.init()
    def Callback(TP_INT):
                Flag = 1
                touch.get_point()
                
    touch.int_irq(Callback)
    touch.Set_Mode(Mode)
    touch.get_point()
    while True:

            X = touch.X_point
            Y = touch.Y_point
                    
            r = 25
            r1 = 25
            x, y = 70, 60
            x1, y1 = 172, 60
            x2, y2 = 120, 120
            x3, y3 = 100, 190
            x4, y4 = 140, 190

            r2 = 12
            x5, y5 = 70, 60
            x6, y6 = 172, 60
                    
            image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
            draw2 = ImageDraw.Draw(image2)

            draw2.ellipse([(x-r, y-r), (x+r, y+r)], fill = 'orange', outline ='black')
            draw2.ellipse([(x1-r, y1-r), (x1+r, y1+r)], fill = 'orange', outline ='black')
                    
            draw2.ellipse([(x2-r, y2-r), (x2+r, y2+r)], fill = 'red', outline ='black')
                    
            draw2.ellipse([(x3-r, y3-r), (x3+r, y3+r)], fill = 'pink', outline ='pink')
            draw2.ellipse([(x4-r, y4-r), (x4+r, y4+r)], fill = 'pink', outline ='pink')

            draw2.arc((1,1,240,240),0, 360, fill =(255,51,153), width=9)
            disp.ShowImage(image2)
                        
                    
            if X >= 92 and X <= 137 and Y >= 85 and Y <= 132:
                         print("nose touch")
                         draw2.arc((1,1,240,240),0, 360, fill ='yellow', width=9)
                         x7, y7 = 70, 70
                         x8, y8 = 172, 70
                         
                         draw2.ellipse([(x7-r2, y7-r2), (x7+r2, y7+r2)], fill = 'black', outline ='pink')
                         draw2.ellipse([(x8-r2, y8-r2), (x8+r2, y8+r2)], fill = 'black', outline ='pink')
                        
                         disp.ShowImage(image2)

            elif X >= 48 and X <= 75 and Y >= 30 and Y <= 70:
                        draw2.ellipse([(X-r2, Y-r2), (X+r2, Y+r2)], fill = 'black', outline ='pink')
                        
                        draw2.ellipse([(x6-r2, y6-r2), (x6+r2, y6+r2)], fill = 'black', outline ='pink')
                        
                        disp.ShowImage(image2)

            elif X >= 147 and X <= 185 and Y >= 30 and Y <= 70:
                        draw2.ellipse([(X-r2, Y-r2), (X+r2, Y+r2)], fill = 'black', outline ='pink')

                        draw2.ellipse([(x5-r2, y5-r2), (x5+r2, y5+r2)], fill = 'black', outline ='pink')
                        
                        disp.ShowImage(image2)
                        

            elif X >= 11 and X <= 79 and Y >= 83 and Y <= 151:
                        print("left cheek touch")
                        x9, y9 = 60, 67
                        x10, y10 = 162, 67
                        
                        draw2.ellipse([(x9-r2, y9-r2), (x9+r2, y9+r2)], fill = 'black', outline ='pink')
                        draw2.ellipse([(x10-r2, y10-r2), (x10+r2, y10+r2)], fill = 'black', outline ='pink')                        
                        
                        disp.ShowImage(image2)
                        

            elif X >= 150 and X <= 214 and Y >= 85 and Y <= 151:
                        print("right cheek touch")
                        x11, y11 = 80, 66
                        x12, y12 = 182, 66
                        
                        draw2.ellipse([(x11-r2, y11-r2), (x11+r2, y11+r2)], fill = 'black', outline ='pink')
                        draw2.ellipse([(x12-r2, y12-r2), (x12+r2, y12+r2)], fill = 'black', outline ='pink')                        
                        
                        disp.ShowImage(image2)

            elif X >= 97 and X <= 131 and Y >= 6 and Y <= 65:
                        print("head touch")
                        x13, y13 = 79, 50
                        x14, y14 = 162, 51
                        
                        draw2.ellipse([(x13-r2, y13-r2), (x13+r2, y13+r2)], fill = 'black', outline ='pink')
                        draw2.ellipse([(x14-r2, y14-r2), (x14+r2, y14+r2)], fill = 'black', outline ='pink')                        
                        
                        disp.ShowImage(image2)
                        
            else:
                        draw2.ellipse([(x5-r2, y5-r2), (x5+r2, y5+r2)], fill = 'black', outline ='pink')
                        draw2.ellipse([(x6-r2, y6-r2), (x6+r2, y6+r2)], fill = 'black', outline ='pink')
                        disp.ShowImage(image2)
                        
except KeyboardInterrupt:
    disp.module_exit()
    exit()

