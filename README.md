![image_1](https://github.com/user-attachments/assets/a343192a-9128-4dd3-b9a4-af106802b5b8)

# Introduction
This repository is dedicated to teaching the basics of microcontrollers to someone who is unfamiliar with the devices. We will be using an ESP32 as the microcontroller basis for this repository (see image above), but do know that there are many different microcontrollers out there, such as:

* Raspberry Pi Pico
* Arduino Uno
* Arduino Nano
* Seeed Studio XIAO


And those are just a few of many ...

This repository requires the following items:
* [ESP32 Microcontroller](https://www.amazon.com/dp/B0D8T53CQ5/?coliid=I225DWGZLOW2SQ&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [220 Ohm Resistors](https://www.amazon.com/dp/B07QK9ZBVZ/?coliid=IGSK77YLFREL&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [LEDs](https://www.amazon.com/dp/B07PG84V17/?coliid=I1UPG7O7VZCMNC&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [Active Buzzers](https://www.amazon.com/dp/B07VRK7ZPF/?coliid=I3QGFJB1KAELXN&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [Passive Buzzers](https://www.amazon.com/dp/B01NCOXB2Q/?coliid=IYMLVIJZBFX9T&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [Air Quality Sensors (MQ-135)](https://www.amazon.com/dp/B07L73VTTY/?coliid=I22PK4I28P0H10&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [LDR](https://www.amazon.com/dp/B099N5W9F7/?coliid=I28VETUTQLT4U5&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [AHT10](https://www.amazon.com/dp/B092495GZJ/?coliid=I3Q06S9CW7IX3P&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [Proximity Sensor (also known as an Obstacle Avoidance Sensor)](https://www.amazon.com/dp/B07W97H2WS/?coliid=I3058QAU9QEZAU&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [Servo](https://www.amazon.com/dp/B0CP98TZJ2/?coliid=IJEW7H1WJO2P&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [DC Motor](https://www.amazon.com/dp/B0DK76KQ8L/?coliid=I16YF5983DPBCY&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [DC Motor Driver](https://www.amazon.com/dp/B08GLQGQ8S/?coliid=I3FZRYQZ0U4MK9&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [0.96 Inch OLED Screen](https://www.amazon.com/dp/B0BFD4X6YV/?coliid=I14P8CIVDG7N7L&colid=15DOEIE96WUTP&ref_=list_c_wl_lv_ov_lig_dp_it&th=1)
* [Breadboards](https://www.amazon.com/dp/B01EV6LJ7G/?coliid=I359UASJIF459G&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)
* [Jumper Cables](https://www.amazon.com/dp/B01EV70C78/?coliid=I5OQSRF0E8IM6&colid=15DOEIE96WUTP&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it)

We will be using Thonny as the IDE (Integrated Development Environment) of choice for us and MicroPython as the language of choice for communicating with the ESP32. To download Thonny, please go to the official [Thonny](https://thonny.org/) website and download the application. Then, depending on your operating system, continue as follows:

**For Windows**: Install the 64-bit version. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Windows. Once downloaded, use the x64 .exe file to install the driver. \
**For Mac**: Install using the first option with .pkg. Then, go to this [website](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) to install a driver, which will allow USB access to Thonny so it can connect to the ESP32 via USB. Go to Downloads, then click CP210x VCP Mac OSX Driver. Then click on the .dmg file to install; **it will ask you to give access at some point in the settings, make sure to allow it access otherwise it won’t work**. \
**For Linux**: It is recommended that you use the flatpak installation method if you already have flatpak in your system. If you do not have flatpak in your system, you may install it from the terminal via your default package manager; see this [website](https://flatpak.org/setup/) for specific directions if you are unsure. You may need to use “sudo chmod a+rw /dev/ttyUSB0” to open up the USB connection each time you connect the ESP32.
One of the first things you need to do with Thonny is to configure it. On the bottom right corner of it, you will find the Interpreter have it set for MicroPython (ESP32). You may need to install this on the ESP32 if it doesn't come with it so make sure to follow directions on flashing MicroPython to it (usually it's just holding down the button). Once it's configured, this is what you'll see:

![image_2](https://github.com/user-attachments/assets/cad9482e-0342-41a9-8ec0-64639c6cf4dd)

You will then be ready to move onto the following sections.

# ESP32 Pin Out
The ESP32 Pin Out is super handy to have, especially when you're trying to find which pins are analog or have PWM capabilities (for motors). See the below image for reference.

![image_3](https://github.com/user-attachments/assets/d906f121-c0f6-41e2-b117-8aa0d213a39f)

# Introductory Scripts
These scripts are meant to be used to learn the foundation of how to interface with MicroPython through an ESP32.

You will find the following scripts in the Introductory Scripts folder:

**Output Sensors**:
* blinking_led.py
* dc_motor.py
* servo.py
* passive_buzzer.py
* active_buzzer.py

**Input Sensors**:
* ldr_led.py
* aht10.py & ahtx0.py
* proximity_sensor.py
* air_quality.py

Please note that for aht10.py and ahtx0.py, the former should be run on Thonny and the latter should be saved to the ESP32 microcontroller to run.

## Example Set-Up
You should use a breadboard to make the connections required for each of the scripts. As an example, here is the connection set-up for aht10.py:

![image_4](https://github.com/user-attachments/assets/79725622-bfe4-48c0-8069-dc47bc20847a)

And when running, this is what it looks like on Thonny:

![image_5](https://github.com/user-attachments/assets/2652bddb-bbd4-4463-8f23-a8703b16fe4b)

# Screen Scripts
There are only two files in this directory and they are specifically for a small OLED screen (.96"). Of course, there is a large variety of screen types that can be used with microcontrollers. For example:

* E-ink Screens (these are really useful because they consume very little power and can hold an image without power)
* TFT Screens (the benefit for these screens lies in the large array of colors for pixels and the fact that many of them are also touch-sensitive)
* LCD Screens (these have the added benefit of a backlight compared to E-ink screens and can come with a variety of colors)

For the purposes of this introduction to screens, only one is included, however (the aforementioned OLED screen). A set-up for this is shown below.

## Example Set-Up
The breadboard set-up is similar to ahtx0.py because this also operates on I2C. Below you can see what the connection looks like with the code running:

![image_6](https://github.com/user-attachments/assets/c0ddd12b-a992-471d-a932-c7fb9450ff8f)

And on the Thonny end:

![image_7](https://github.com/user-attachments/assets/a6a14373-d0b0-4f55-83d8-b50839043880)

# Custom PCBs

![image_8](https://github.com/user-attachments/assets/e39cd048-fa17-4853-8db5-6af9e7af20ad)


A few custom PCBs are also included here, with their Gerber files for requesting their manufacture included in a separate folder. You can see the front of these PCBs above and the backside below.

![image_9](https://github.com/user-attachments/assets/9054134c-aa21-48a9-aed5-546b77fd59c8)

The following scripts are included in the Custom PCBs .py Files folder:

* Active-Passive-Buzzer-with-Two-Buttons.py
* LED-with-Push-Button.py
* Motor-with-Motor-Drive.py
* Servo-with-Push-Button.py

Each custom PCB has a name that corresponds to the file written on it. However, please note that it is required to solder the headers - female and/or male - to the PCBs prior to using them. I soldered mine using a Hakko soldering iron at 800F, but it can be done with any soldering iron and probably at a lower temperature.

# Thank You
Thank you for visiting this repository or using it to learn how to use an ESP32 with MicroPython.
