# Kratos Rover

## Components/Overall Design

- Jetson Nano 2GB for object detection, steamming, and wireless input.
- STM32 for low level control. (also use RTOS for monitoring evething) 
- Communication between Jetson and STM32 (I2C, SPI or UART)
- [Looking for a camera](https://www.accessoriestested.com/best-camera-for-nvidia-jetson-nano/)
- Use two motors on the sides
- Power Distribution board? might not be needed
- Battery
- maybe a servo to look around?
- a smartphone/tablet 

### program the arduino from the raspberry pi
implement this to give the main computer onboard to update the software on the microcontroller

- article: <https://siytek.com/arduino-cli-raspberry-pi/>
- more: <https://ladvien.com/headless-programming-ardunio-via-rpi/>
- possible solutions:
	- <https://www.instructables.com/AVRArduino-Flashing-With-Raspberry-Pi/>
	- <https://www.monocilindro.com/2017/03/20/flashing-arduino-using-raspberry-pi-shell/>


