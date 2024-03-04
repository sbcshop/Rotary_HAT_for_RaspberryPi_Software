# Rotary_HAT_for_RaspberryPi_Software
<!--
<img src = "https://github.com/sbcshop/Rotary_Pico-W_Powered_Software/blob/main/images/pico.png" width="648" height="432">
-->

This GitHub page offers a interfacing details and getting started guide of Rotary Encoder HAT for Raspberry Pi.

### Features : 
- Compatible with Rasberry Pi Boards
- It has a Rotary encoder
- 1.28" TFT display with a resolution of 240 x 240 pixels for visual interactions
- Round display has capacitive touch

<!--
### Interfacing Details
- Pico W and Touch interfacing
  
  | Pico W | Touch Controller| Function |
  |---|---|---|
  |GP6 | SDA | Touch I2C  |
  |GP7 | SCL  | Touch I2C  |
  |GP4 | RESET  | Touch Reset  |
  |GP7 | INT  | Touch Intrrupt  |

  
- Pico W and Round Display interfacing
  
  | Pico W | Display Pin | Function |
  |---|---|---|
  |GP10 | SCLK  | Clock pin of SPI interface for display|
  |GP11 | DIN   | MOSI (Master OUT Slave IN) data pin of SPI interface|
  |GP12 | DOUT   | MISO (Master OUT Slave OUT) data pin of SPI interface|
  |GP8  | DC    | Data/Command pin of SPI interface|
  |GP13 | CS    | Chip Select pin of SPI interface for display|
  |GP9  | Reset | Display Reset Pin |
  |GP14 | BL    | Display backlight Pin |
 
- RGBLed Interfacing with Pico W
  | Pico W | RGB LED | Function |
  |---|---|---|
  | GP15 | DIN | WS2812 Data Pin|

- Rotary Encoder Interfacing with Pico W
  | RPi | Encoder |
  |---|---|
  | GPIO6 | OUT A | 
  | GPIO13 | OUT B | 


### 1. Setup Raspberry Pi
  
### 2. 

### Example Codes
   Save whatever example code file you want to try as **main.py** in **Pico W** as shown above [step 3](https://github.com/sbcshop/Rotary_Pico-W_Powered_Software/tree/main?tab=readme-ov-file#3-how-to-move-your-script-on-pico-w-of-rotart-pico-w), also add related lib files with the default name.
   In [example](https://github.com/sbcshop/Rotary_Pico-W_Powered_Software/tree/main/examples) folder you will find demo example script code to test onboard components of Rotary Pico W like 
   - [Library](https://github.com/sbcshop/Rotary_Pico-W_Powered_Software/tree/main/examples/library): before running the code kindly save this library inside Pico W.
   - [Display test, RGB test, SD Card test, and touch test, etc.](https://github.com/sbcshop/Rotary_Pico-W_Powered_Software/tree/main/examples/Demo%20Codes): All demo file
   - [Image display test](https://github.com/sbcshop/Rotary_Pico-W_Powered_Software/tree/main/examples/image%20display): testing image display.

-->

## Resources
  * [Schematic](https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Hardware/blob/main/Design%20Data/SCH%20Rotary%20Encoder%20Hat.pdf)
  * [Hardware Files](https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Hardware)
  * [Step File](https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Hardware/blob/main/Mechanical%20Data/Rotary%20Encoder%20HAT.step)
  * [Raspberry Pi Getting Started](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started)
  * [Raspberry Pi Configuration](https://www.raspberrypi.com/documentation/computers/configuration.html)

## Related Products
  * [1.28 round touch lcd hat](https://shop.sb-components.co.uk/products/1-28-round-touch-lcd-hat-for-raspberry-pi?_pos=8&_sid=b964c85bf&_ss=r) 
   
     ![1.28 round touch lcd hat](https://shop.sb-components.co.uk/cdn/shop/files/shopimages_87b6d1ec-2c95-4621-a07f-5937a8d8c090.png?v=1687857703&width=300)   

  * [Roundy](https://shop.sb-components.co.uk/products/roundy?_pos=1&_sid=b964c85bf&_ss=r) 
   
     ![Roundy](https://shop.sb-components.co.uk/cdn/shop/products/roundypi.png?v=1650457581&width=300) 

  * [Round LCD HAT](https://shop.sb-components.co.uk/products/round-lcd-hat-for-raspberry-pi?_pos=2&_sid=b964c85bf&_ss=r) 
   
     ![Round LCD HAT](https://shop.sb-components.co.uk/cdn/shop/products/LCDHATforPi.jpg?v=1619171154&width=300)

  * [1.28” Round LCD Breakout](https://shop.sb-components.co.uk/products/1-28-round-lcd-breakout?_pos=5&_sid=b964c85bf&_ss=r) 
   
     ![1.28” Round LCD Breakout](https://shop.sb-components.co.uk/cdn/shop/products/01_a58fb20c-7cc7-4908-bfca-549b28c721b6.png?v=1677234693&width=300)

 
## Product License

This is ***open source*** product. Kindly check the LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
