''' Library File '''
import os
import sys
import time
import spidev
import smbus
import logging
import numpy as np

class RaspberryPi:
    def __init__(self,spi=spidev.SpiDev(0,0),spi_freq=40000000,rst = 27,dc = 25,bl = 18,tp_int = 4,tp_rst = 23,bl_freq=1000):
        import RPi.GPIO      
        self.np=np
        self.RST_PIN= rst
        self.DC_PIN = dc
        self.BL_PIN = bl

        self.TP_INT = tp_int
        self.TP_RST = tp_rst

        self.X_point = self.Y_point = self.Gestures = 0

        self.SPEED  =spi_freq
        self.BL_freq=bl_freq
        self.GPIO = RPi.GPIO

        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setwarnings(False)
      
        #Initialize SPI
        self.SPI = spi
        
        # #Initialize I2C
        self.I2C = smbus.SMBus(1)
        self.address = 0x15

       

    def digital_write(self, pin, value):
        self.GPIO.output(pin, value)

    def digital_read(self, pin):
        return self.GPIO.input(pin)

    def int_irq(self,Int_Callback):
        self.GPIO.add_event_detect(self.TP_INT,self.GPIO.FALLING,Int_Callback,5) 

    def delay_ms(self, delaytime):
        time.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        if self.SPI!=None :
            self.SPI.writebytes(data)

    def Touch_module_init(self):

        self.GPIO.setup(self.TP_INT,    self.GPIO.IN,self.GPIO.PUD_UP)
        self.GPIO.setup(self.TP_RST,    self.GPIO.OUT)


    def i2c_write_byte(self, Addr, val):
        self.I2C.write_byte_data(self.address, Addr, val)

    def i2c_read_byte(self,Addr):
        return self.I2C.read_byte_data(self.address, Addr)

    def bl_DutyCycle(self, duty):
        self._pwm.ChangeDutyCycle(duty)
        
    def bl_Frequency(self,freq):
        self._pwm.ChangeFrequency(freq)

    def LCD_module_init(self):
        self.GPIO.setup(self.RST_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.DC_PIN, self.GPIO.OUT)
        self.GPIO.setup(self.BL_PIN, self.GPIO.OUT)

        self._pwm=self.GPIO.PWM(self.BL_PIN,self.BL_freq)
        self._pwm.start(100)
        if self.SPI!=None :
            self.SPI.max_speed_hz = self.SPEED        
            self.SPI.mode = 0b00    

        return 0

    def module_exit(self):
        if self.SPI!=None :
            self.SPI.close()
        
        if self.I2C!=None :
            self.I2C.close()
        
        self.GPIO.output(self.RST_PIN, 1)
        self.GPIO.output(self.DC_PIN, 0) 

        self.GPIO.output(self.TP_RST, 1)   
           
        self._pwm.stop()
        time.sleep(0.001)
        self.GPIO.output(self.BL_PIN, 1)
        #self.GPIO.cleanup()

class lcd(RaspberryPi):

    width = 240
    height = 240 
    def LCD_WriteReg(self, cmd):
        self.digital_write(self.DC_PIN, self.GPIO.LOW)
        self.spi_writebyte([cmd])
        
    def LCD_WriteData_Byte(self, val):
        self.digital_write(self.DC_PIN, self.GPIO.HIGH)
        self.spi_writebyte([val])
        
    def LCD_Reset(self):
        """Reset the display"""
        self.GPIO.output(self.RST_PIN,self.GPIO.HIGH)
        time.sleep(0.01)
        self.GPIO.output(self.RST_PIN,self.GPIO.LOW)
        time.sleep(0.01)
        self.GPIO.output(self.RST_PIN,self.GPIO.HIGH)
        time.sleep(0.01)
        
    def Init(self):
        """Initialize dispaly"""  
        self.LCD_module_init()   
        self.LCD_Reset()
        
        self.LCD_WriteReg(0xEF)
        self.LCD_WriteReg(0xEB)
        self.LCD_WriteData_Byte(0x14)
        
        self.LCD_WriteReg(0xFE)			 
        self.LCD_WriteReg(0xEF) 

        self.LCD_WriteReg(0xEB)	
        self.LCD_WriteData_Byte(0x14)

        self.LCD_WriteReg(0x84)			
        self.LCD_WriteData_Byte(0x40) 

        self.LCD_WriteReg(0x85)			
        self.LCD_WriteData_Byte(0xFF)

        self.LCD_WriteReg(0x86)			
        self.LCD_WriteData_Byte(0xFF) 

        self.LCD_WriteReg(0x87)		
        self.LCD_WriteData_Byte(0xFF)

        self.LCD_WriteReg(0x88)			
        self.LCD_WriteData_Byte(0x0A)

        self.LCD_WriteReg(0x89)			
        self.LCD_WriteData_Byte(0x21)

        self.LCD_WriteReg(0x8A)		
        self.LCD_WriteData_Byte(0x00)

        self.LCD_WriteReg(0x8B)			
        self.LCD_WriteData_Byte(0x80) 

        self.LCD_WriteReg(0x8C)			
        self.LCD_WriteData_Byte(0x01) 

        self.LCD_WriteReg(0x8D)			
        self.LCD_WriteData_Byte(0x01) 

        self.LCD_WriteReg(0x8E)			
        self.LCD_WriteData_Byte(0xFF) 

        self.LCD_WriteReg(0x8F)			
        self.LCD_WriteData_Byte(0xFF) 


        self.LCD_WriteReg(0xB6)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x20)

        self.LCD_WriteReg(0x36)
        self.LCD_WriteData_Byte(0x08)
    
        self.LCD_WriteReg(0x3A)			
        self.LCD_WriteData_Byte(0x05) 


        self.LCD_WriteReg(0x90)			
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x08) 

        self.LCD_WriteReg(0xBD)			
        self.LCD_WriteData_Byte(0x06)
	
        self.LCD_WriteReg(0xBC)			
        self.LCD_WriteData_Byte(0x00)	

        self.LCD_WriteReg(0xFF)			
        self.LCD_WriteData_Byte(0x60)
        self.LCD_WriteData_Byte(0x01)
        self.LCD_WriteData_Byte(0x04)

        self.LCD_WriteReg(0xC3)			
        self.LCD_WriteData_Byte(0x13)
        self.LCD_WriteReg(0xC4)			
        self.LCD_WriteData_Byte(0x13)

        self.LCD_WriteReg(0xC9)		
        self.LCD_WriteData_Byte(0x22)

        self.LCD_WriteReg(0xBE)			
        self.LCD_WriteData_Byte(0x11)

        self.LCD_WriteReg(0xE1)		
        self.LCD_WriteData_Byte(0x10)
        self.LCD_WriteData_Byte(0x0E)

        self.LCD_WriteReg(0xDF)			
        self.LCD_WriteData_Byte(0x21)
        self.LCD_WriteData_Byte(0x0c)
        self.LCD_WriteData_Byte(0x02)

        self.LCD_WriteReg(0xF0)   
        self.LCD_WriteData_Byte(0x45)
        self.LCD_WriteData_Byte(0x09)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x26)
        self.LCD_WriteData_Byte(0x2A)

        self.LCD_WriteReg(0xF1)    
        self.LCD_WriteData_Byte(0x43)
        self.LCD_WriteData_Byte(0x70)
        self.LCD_WriteData_Byte(0x72)
        self.LCD_WriteData_Byte(0x36)
        self.LCD_WriteData_Byte(0x37)  
        self.LCD_WriteData_Byte(0x6F)


        self.LCD_WriteReg(0xF2)   
        self.LCD_WriteData_Byte(0x45)
        self.LCD_WriteData_Byte(0x09)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x26)
        self.LCD_WriteData_Byte(0x2A)

        self.LCD_WriteReg(0xF3)  
        self.LCD_WriteData_Byte(0x43)
        self.LCD_WriteData_Byte(0x70)
        self.LCD_WriteData_Byte(0x72)
        self.LCD_WriteData_Byte(0x36)
        self.LCD_WriteData_Byte(0x37) 
        self.LCD_WriteData_Byte(0x6F)

        self.LCD_WriteReg(0xED)	
        self.LCD_WriteData_Byte(0x1B) 
        self.LCD_WriteData_Byte(0x0B) 

        self.LCD_WriteReg(0xAE)			
        self.LCD_WriteData_Byte(0x77)
	
        self.LCD_WriteReg(0xCD)			
        self.LCD_WriteData_Byte(0x63)		


        self.LCD_WriteReg(0x70)			
        self.LCD_WriteData_Byte(0x07)
        self.LCD_WriteData_Byte(0x07)
        self.LCD_WriteData_Byte(0x04)
        self.LCD_WriteData_Byte(0x0E) 
        self.LCD_WriteData_Byte(0x0F)
        self.LCD_WriteData_Byte(0x09)
        self.LCD_WriteData_Byte(0x07)
        self.LCD_WriteData_Byte(0x08)
        self.LCD_WriteData_Byte(0x03)

        self.LCD_WriteReg(0xE8)			
        self.LCD_WriteData_Byte(0x34)

        self.LCD_WriteReg(0x62)			
        self.LCD_WriteData_Byte(0x18)
        self.LCD_WriteData_Byte(0x0D)
        self.LCD_WriteData_Byte(0x71)
        self.LCD_WriteData_Byte(0xED)
        self.LCD_WriteData_Byte(0x70)
        self.LCD_WriteData_Byte(0x70)
        self.LCD_WriteData_Byte(0x18)
        self.LCD_WriteData_Byte(0x0F)
        self.LCD_WriteData_Byte(0x71)
        self.LCD_WriteData_Byte(0xEF)
        self.LCD_WriteData_Byte(0x70) 
        self.LCD_WriteData_Byte(0x70)

        self.LCD_WriteReg(0x63)			
        self.LCD_WriteData_Byte(0x18)
        self.LCD_WriteData_Byte(0x11)
        self.LCD_WriteData_Byte(0x71)
        self.LCD_WriteData_Byte(0xF1)
        self.LCD_WriteData_Byte(0x70) 
        self.LCD_WriteData_Byte(0x70)
        self.LCD_WriteData_Byte(0x18)
        self.LCD_WriteData_Byte(0x13)
        self.LCD_WriteData_Byte(0x71)
        self.LCD_WriteData_Byte(0xF3)
        self.LCD_WriteData_Byte(0x70) 
        self.LCD_WriteData_Byte(0x70)

        self.LCD_WriteReg(0x64)			
        self.LCD_WriteData_Byte(0x28)
        self.LCD_WriteData_Byte(0x29)
        self.LCD_WriteData_Byte(0xF1)
        self.LCD_WriteData_Byte(0x01)
        self.LCD_WriteData_Byte(0xF1)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x07)

        self.LCD_WriteReg(0x66)			
        self.LCD_WriteData_Byte(0x3C)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0xCD)
        self.LCD_WriteData_Byte(0x67)
        self.LCD_WriteData_Byte(0x45)
        self.LCD_WriteData_Byte(0x45)
        self.LCD_WriteData_Byte(0x10)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x00)

        self.LCD_WriteReg(0x67)			
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x3C)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x01)
        self.LCD_WriteData_Byte(0x54)
        self.LCD_WriteData_Byte(0x10)
        self.LCD_WriteData_Byte(0x32)
        self.LCD_WriteData_Byte(0x98)

        self.LCD_WriteReg(0x74)			
        self.LCD_WriteData_Byte(0x10)	
        self.LCD_WriteData_Byte(0x85)	
        self.LCD_WriteData_Byte(0x80)
        self.LCD_WriteData_Byte(0x00) 
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(0x4E)
        self.LCD_WriteData_Byte(0x00)					
        
        self.LCD_WriteReg(0x98)		
        self.LCD_WriteData_Byte(0x3e)
        self.LCD_WriteData_Byte(0x07)

        self.LCD_WriteReg(0x35)	
        self.LCD_WriteReg(0x21)

        self.LCD_WriteReg(0x11)
        time.sleep(0.12)
        self.LCD_WriteReg(0x29)
        time.sleep(0.02)
  
    def SetWindows(self, Xstart, Ystart, Xend, Yend):
        #set the X coordinates
        self.LCD_WriteReg(0x2B)
        self.LCD_WriteData_Byte(0x00)               #Set the horizontal starting point to the high octet
        self.LCD_WriteData_Byte(Ystart)      #Set the horizontal starting point to the low octet
        self.LCD_WriteData_Byte(0x00)               #Set the horizontal end to the high octet
        self.LCD_WriteData_Byte(Xend - 1) #Set the horizontal end to the low octet 
        
        #set the Y coordinates
        self.LCD_WriteReg(0x2A)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(Xstart)
        self.LCD_WriteData_Byte(0x00)
        self.LCD_WriteData_Byte(Yend - 1)

        self.LCD_WriteReg(0x2C) 

    def ShowImage_Windows(self,Xstart,Ystart,Xend,Yend,Image):
        imwidth, imheight = Image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))
        img = self.np.asarray(Image)
        pix = self.np.zeros((self.width,self.height,2), dtype = self.np.uint8)
        pix[...,[0]] = self.np.add(self.np.bitwise_and(img[...,[0]],0xF8),self.np.right_shift(img[...,[1]],5))
        pix[...,[1]] = self.np.add(self.np.bitwise_and(self.np.left_shift(img[...,[1]],3),0xE0),self.np.right_shift(img[...,[2]],3))
        pix = pix.flatten().tolist()

        if Xstart > Xend:
            data = Xstart
            Xstart = Xend
            Xend = data
            
        if (Ystart > Yend):        
            data = Ystart
            Ystart = Yend
            Yend = data
            
        if Xstart <= 10:
            Xstart = 10
        if Ystart <= 10:
            Ystart = 10
            
        Xstart -= 10;Xend += 10
        Ystart -= 10;Yend += 10
        
        self.SetWindows ( Xstart, Ystart, Xend, Yend)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range (Ystart,Yend-1):             
            Addr = (Xstart * 2) + (i * 240 * 2)                
            self.spi_writebyte(pix[Addr : Addr+((Xend-Xstart)*2)])


    def ShowImage(self,Image):
        imwidth, imheight = Image.size
        if imwidth != self.width or imheight != self.height:
            raise ValueError('Image must be same dimensions as display \
                ({0}x{1}).' .format(self.width, self.height))
        img = self.np.asarray(Image)
        pix = self.np.zeros((self.width,self.height,2), dtype = self.np.uint8)
        pix[...,[0]] = self.np.add(self.np.bitwise_and(img[...,[0]],0xF8),self.np.right_shift(img[...,[1]],5))
        pix[...,[1]] = self.np.add(self.np.bitwise_and(self.np.left_shift(img[...,[1]],3),0xE0),self.np.right_shift(img[...,[2]],3))
        pix = pix.flatten().tolist()
        self.SetWindows ( 0, 0, self.width, self.height)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range(0,len(pix),4096):
            self.spi_writebyte(pix[i:i+4096])		
    
    def clear(self):
        _buffer = [0xff]*(self.width * self.height * 2)
        self.SetWindows ( 0, 0, self.width, self.height)
        self.digital_write(self.DC_PIN,self.GPIO.HIGH)
        for i in range(0,len(_buffer),4096):
            self.spi_writebyte(_buffer[i:i+4096])	        
        
class touch(RaspberryPi):
    def init(self):
        self.Touch_module_init()   
        self.Touch_Reset()

        bRet = self.WhoAmI()
        if bRet:
            Rev = self.Read_Revision()
            print("CST816T Revision = %d."%Rev)
            self.Stop_Sleep()
        else:
            return False

    def Touch_Write_Byte(self, cmd, val):
        self.i2c_write_byte(cmd, val)

    def Touch_Read_Byte(self, cmd):
        return self.i2c_read_byte(cmd)

    def WhoAmI(self):
        if (0xB5) != self.Touch_Read_Byte(0xA7):
            return False
        return True

    def Read_Revision(self):
        return self.Touch_Read_Byte(0xA9)

    def Stop_Sleep(self):
        self.Touch_Write_Byte(0xFE,0x01)
    
    def Touch_Reset(self):
        self.GPIO.output(self.TP_RST,self.GPIO.LOW)
        time.sleep(0.01)
        self.GPIO.output(self.TP_RST,self.GPIO.HIGH)
        time.sleep(0.05) 

    #Set mode     
    def Set_Mode(self,mode,callback_time=10,rest_time=5): 
        # mode = 0 gestures mode 
        # mode = 1 point mode 
        # mode = 2 mixed mode 
        if (mode == 1):      
            self.Touch_Write_Byte(0xFA,0X41)
            
        elif (mode == 2) :
            self.Touch_Write_Byte(0xFA,0X71)
            
        else:
            self.Touch_Write_Byte(0xFA,0X11)
            self.Touch_Write_Byte(0xEC,0X01)
     
    #Get the coordinates of the touch  
    def get_point(self):
        xy_point = [0,0,0,0]

        xy_point[0] = self.Touch_Read_Byte(0x03)
        xy_point[1] = self.Touch_Read_Byte(0x04)
        xy_point[2] = self.Touch_Read_Byte(0x05)
        xy_point[3] = self.Touch_Read_Byte(0x06)
        
        x_point= ((xy_point[0]&0x0f)<<8)+xy_point[1]
        y_point= ((xy_point[2]&0x0f)<<8)+xy_point[3]
        
        self.X_point=x_point
        self.Y_point=y_point

