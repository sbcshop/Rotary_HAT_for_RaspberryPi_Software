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


### Interfacing Details
<img src = "https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software/blob/main/images/Rotary_HAT_Interfacing.png" width="693" height="468">


### 1. Setup Raspberry Pi
- You need to setup your Raspberry Pi, for this visit their [official site here](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- Once done now confiure Raspberry Pi to use with Rotary Encoder HAT
- You have to enable I2C, SPI communication. To do this, run the command ```sudo raspi-config```. 

  <img src = "https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software/blob/main/images/sudo_raspi_config.png" width="295" height="70">

- This opens the Raspberry Pi user interface (UI), where you can configure different Raspberry Pi settings.
  
  <img src = "https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software/blob/main/images/raspi_config.png" width="450" height="259">

- Enable SPI interface needed for display Hardware

  <img src = "https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software/blob/main/images/SPI_enable.png" width="538" height="376">

- In similar way enable I2C interface needed for Touch hardware

  
### 2. Running Examples
- This repo contains various [examples](https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software/tree/main/example) to test onboard components of Rotary HAT and other interesting demo for experimental purpose which you can modify for applications.
- To try examples simply download or git clone this repository into your Pi,
  
```
git clone https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software
```

  <img src = "https://github.com/sbcshop/Rotary_HAT_for_RaspberryPi_Software/blob/main/images/clone_repo.png" width="651" height="237">

- Open anyone example into python IDE and run the code to see in action, modify build and share your creation.

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
