'''Demo for Testing Rotary Encoder of HAT '''
from RPi import GPIO
from time import sleep
import os
import sys 
import time
import spidev as SPI
sys.path.append("..")
from lib import Round_Touch
from PIL import Image,ImageDraw,ImageFont

#define encoder pins
clk = 13		
dt = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:
        disp = Round_Touch.lcd()
        disp.Init()
        disp.clear()  
        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print (counter)
                        if counter == 1:
                                    image = Image.open('../pic/img1.jpg')	
                                    im_r2=image.rotate(0)
                                    disp.ShowImage(im_r2)
                                    print("UP")

                        elif counter == 2:                                 
                                    image = Image.open('../pic/img6.jpg')	
                                    im_r2=image.rotate(0)
                                    disp.ShowImage(im_r2)
                                    print("DOWN")
                                            
                                            
                        elif counter  == 3:
                                    image = Image.open('../pic/img7.jpg')	
                                    im_r2=image.rotate(0)
                                    disp.ShowImage(im_r2)
                                    print("LEFT")     
                              
                                            
                        elif counter == 4:
                                    image = Image.open('../pic/img2.jpg')	
                                    im_r2=image.rotate(0)
                                    disp.ShowImage(im_r2)
                                    print("RIGHT") 

                        elif counter == 5:
                                    image = Image.open('../pic/img4.jpg')	
                                    im_r2=image.rotate(0)
                                    disp.ShowImage(im_r2)
                                    print("LONG PRESS") 
                              
                                            
                        elif counter == 6:
                                    image = Image.open('../pic/img8.jpg')	
                                    im_r2=image.rotate(0)
                                    disp.ShowImage(im_r2)
                                    print("DOUBLE TAB")
                                    count =0
                        
                clkLastState = clkState
                sleep(0.01)
finally:
        GPIO.cleanup()
