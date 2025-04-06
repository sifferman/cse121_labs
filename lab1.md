# Lab 1 - Lab Setup and trivial tests

  

Due Date: Tues 4/11/2025

  

This lab is worth 20 Points. Project check-off takes

place during the TA section.

  

The overall objective of this lab is to setup the Pi4 (lab1.1),

and program a couple of simple ESP32 programs using the Pi4 board

(lab1.2 and lab1.3). This requires having a WIFI setup (eduroam works)

in the Pi4.

  

It is VERY important to submit the report.pdf.

If this file is missing, you lose 1/2 of the points.

  

## Lab1.0: Acquire CSE121 Kit (0 points)

  

You must collect a cse121 kit from BELS' office in JBE-40 (in the basement).

It is yours to borrow for the quarter, then return after finishing the last lab.

If you are missing any parts when you return it, you will have to pay.

  

## Lab1.1: setup Pi4 (10 points)

  

Lab1.1 requires you to assemble the components leading to getting

a working Pi4 module and case, functioning with eduroam WiFi and

and linux.

  

The installation should be based on an **ubuntu server**

(not the Pi4 default). This can be sufficient to complete

the lab. We will also install X-Windows an XFACE desktop

which adds extra user friendly functionality.

  

1. Place the Pi4 into its case. Ground yourself when

handling this card so as to avoid possible failure due

to static electricity. The Pi4 is the most expensive

card in your kit, the case will protect the device.

Protecting electronics against static electricity is always

a good idea. Note that this is a very nice case.

The Pi4's CPU will be in contact with a thermal contact

which eliminates the need for a fan.

  

2. Install a the Pi Imager software into a host computer, so

that we can flash the Operating System into the Pi4 microSD.

Details for downloading Pi Imager for various computer

platforms (Mac, Windows or Linux) can be found here:

<https://www.raspberrypi.com/software/>

  

3. In order to flash the microSD insert it into the CanaKit

"USB MicroSD Card Reader" device.

  

4. Under "Other general-purpose OS", select "Ubuntu" and then select the latest 64-bit Ubuntu Server image. (24.04 and 24.10 are both okay)

(<https://ubuntu.com/download/raspberry-pi>)

  

5. Insert MicroSD Card Reader into a USB Port in the computer.

Start the raspberry-pi imager in order to Flash the microSD

Absolutely make sure that you are selecting the proper drive to format by unplugging and plugging the MicroSD Card Reader back in to see which drive disappears and reappears.

  

6. Extract the microSD from the USB MicroSD Card Reader and

insert it back into the Pi4 box microSD slot.

Connect cables for keyboard, monitor, and mouse.

Power on the device, and allow it to boot. Then type this

to login (unless you changed user name and passwd in the settings):

  

```

login: ubuntu

password: ubuntu

```

  

NOTE: if you might also be able a serial port to connect to the

PI4 UART and a terminal for this part of the setup,

but we reccommend use of a monitor with an HDMI interface.

  

7. If you do an `ls` and find that some colors are unreadable on your monitor, type

  

```bash

vim ~/.bashrc

```

  

Quick vim tutorial:_

  

1.  _Calling vim on a nonexisting file creates a new file at that location._&nbsp;

2.  _To move your cursor to the last character press "shift" + "g"._

3.  _To modify the file, press "i", and adjust cursor using the arrow keys._

4.  _To finish modifying press "Esc"._

5.  _To finish editing, press "shift" + ":", and the console will appear at the bottom of the screen._

6.  _Type "wq" into the terminal to write (save) and quit_

1.  _If you want to quit without saving type "q!"_

  

Then press i to enter the following lines at the bottom of the file

  

```

LS_COLORS=$LS_COLORS:'di=0;36:' ;

export LS_COLORS

```

The number 36 corresponds to teal. Check here to see all formatting options.

> <https://askubuntu.com/questions/466198/how-do-i-change-the-color-for-directories-with-ls-in-the-console>

  

Press "esc", then ":", and type "wq", and "enter" to save the file.

  

Finally to push the change type

  

```bash

source ~/.bashrc

```

  

8. Setup Preliminary Wifi

  

Getting the pi online through eduroam will be necessary for completing lab 1.1, but for now, any of the following methods should work for completing setup.

If you are in lab:

Temporarily plug your pi into the ethernet and move onto step 8.

  

If you are at home follow this tutorial to connect to your home wifi.

> <https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line>

  

9. Upgrade ubuntu and install required packages

  

```bash

sudo apt update

sudo apt upgrade

```

  

10. Install XFCE window manager.

  

This will install a desktop interface like any other computer and is more convenient than just the command line interface (CLI) alone

  

Type the following to install the necessary packages:

  

```bash

sudo apt install xfce4 xinit firefox

```

Then reboot your pi to let the changes take effect. You can unplug your pi and plug back in, or simply type

  

```bash

sudo reboot

```

If attempting to log in prints "Failed to start Session" or you are otherwise unable to log in, continue to step 10.

  

press ctrl + alt + F1, (cmd + alt + F1 for Mac).

  

a. Along with xfce4, install the following

```bash

sudo apt-get install lightdm

sudo apt-get install ubuntu-session

```

  

When installing lightdm, a pink screen will pop up, Select gdm3 instead of lightdm.

  

b. Add your user to the "tty" group using this command replacing username with whatever you picked

```bash

sudo usermod -a -G tty username

```

The usermod APPENDS the tty GROUP to your user account, giving you permission to access&nbsp;your pi4's ports and virtual terminal sessions._

  

If you'd like to learn more about tty click [here](https://www.linusakesson.net/programming/tty/index.php?ref=itsfoss.com)! Basically here its giving us the ability to troubleshoot without the need of a graphical interface._

  

c. Create the file "Xwrapper.config" using the following command.

  

```bash

sudo vim /etc/X11/Xwrapper.config

```

/etc is where all app config files are stored_

d. Insert these lines (case sensitive) in the "Xwrapper.config" file:

```

allowed_users=anybody

needs_root_rights=yes

```

Click [here](https://man.archlinux.org/man/extra/xorg-server/Xwrapper.config.5.en) if you're interested in what these parameters represent._

e. Create the file "lightdm.conf" using the following command.

```bash

sudo vim /etc/lightdm/lightdm.conf

```

f. Add the following lines in the "lightdm.conf" file (the allow-guest line is optional):

```

[SeatDefaults]

allow-guest=false

user-session=xfce

```

g. Rebooting using the following command should successfully launch the desktop:

```bash

sudo reboot

```

  

11. Connect/setup to eduroam (AND INCLUDE IT in report.pdf)

  

Once you're on your desktop, connecting to eduroam is as easy as navigating to the network settings, selecting eduroam as your network, and then signing on using your cruz ID and gold password as you would for any other device.

  

If your settings show "No wifi adapter detected" or does not connect for any other reason, locate the white flashdrive containing eduroam.zip and run the install script using the following steps:

  

a. Install network manager

```

sudo apt install network-manager unzip

```

You'll need unzip package later to unzip eduroam.zip contained in the flash drive.

  

b. Prior to plugging in usb stick run

```

lsblk

```

This will **display details about block devices** so you can tell which one the flash drive is after plugging it in.

  

c. Plug in the usb stick and run:

```

lsblk

```

Identify the new device most likely it'll be **/dev/sda1**

  

d. Make a directory which the usb will be mounted to and mount it:

```

mkdir ~/usb_stick

sudo mount /dev/sda1 ~/usb_stick

```

**/dev/sda1** might be different for you

  

e. Copy the content of the flash drive to you home directory

```

cp -r ~/usb_stick/eduroam.zip ~/.

or

cp -r ~/usb_stick/eduroam ~/.

  

```

f. Unmount the flash drive and remove it:

```

sudo umount /dev/sda1

```

**/dev/sda1** might be different for you

  

g. unzip eduroam.zip and run the eduroam/setup.sh

```

unzip eduroam.zip

cd ~/eduroam

sudo ./setup.sh

```

You might need to chmod +x the script.

  

h. Input your Gold password info when prompted, and you should be connected. Remove you're ethernet and try pinging google.

```

email: blank@ucsc.edu

username: blank@ucsc.edu

password: [Gold password]

```

  
  
  

## Lab1.2: Run hello world in ESP32 (5 points)

  

1. Update and upgrade ubuntu and install required packages

  

```bash

sudo apt update # synchronizes local directory of the latest packages.

sudo apt upgrade # this upgrades packages downloaded to be the latest.

  

# install important packages.

sudo apt-get install fish neovim g++ git wget \

flex bison gperf python3 python3-venv cmake \

ninja-build ccache libffi-dev libssl-dev \

dfu-util libusb-1.0-0

```

  

2. Get ESP32 Software Toolchain

Documentation for the steps here can be found at this website:

<https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html>

  

Perform these steps:

  

```bash

mkdir -p ~/esp

cd ~/esp

git clone --recursive https://github.com/espressif/esp-idf.git

cd ~/esp/esp-idf

./install.sh esp32c3

```

  

WARNING: This is a TOP OF THE TREE checkout. What this means is

that the day that you clone the repo, it may (or not) have a BUG

and thus it may not work. (top of the tree implies that is the

latest entry in the git repository tree).

  

If you end up have difficulties with this or any other parts of this

lab, you should include this in your report.pdf along with all the

gorie details. This code has been known to be quite reliable under

Linux, which is what we are using the Pi4.

  

3. Get simple hello_world running

  

```bash

# Setup (once)

cd ~/esp/esp-idf

. export.sh

cp -a examples/get-started/hello_world ~/esp/

```

  

Patch the hello world (print your name, not mine).

Edit the "hello_world_main.c" so that after printing the

"Minimum free heap..." it prints your name. E.g:

  

```c

printf("Perico Los Palotes\n"); // Substitute your name

```

  

```bash

# Build

cd ~/esp/hello_world

idf.py set-target esp32c3

cd build

ninja

```

  

4. Deploy hello_word

  

Connect the ESP32 board to the raspberry PI4 USB

(Notice ESP32 has a USB-C, must connect to PI4 USB-2 "blue is OK")

  

```bash

idf.py flash

idf.py monitor

# (to  stop  monitor  ctrl+])

```

  

## Lab1.3: Flash LED on ESP32 (5 Points)

  

The ESP32C3 board that has a LED connected to GPIO2. Write a simple C program

that flashes the LED on/off once per second.

  

The app_main should call something like this:

  

```c

xTaskCreate(blink_task, "blink_task", 2048, NULL, 5, NULL);

```

  

This means that it needs to use FreeRTOS.

  

## What/How to submit

  

Create a zip file of your project source code (**DO NOT INCLUDE

the BUILD DIRECTORY**), then upload to Gradescope. Lab1.2 and lab1.3

should have different directories (lab1_2 and lab1_3). For

example, these are the lab files and directories for my lab1.3.

  

* report.pdf

* lab1_2/sdkconfig

* lab1_2/CMakeLists.txt

* lab1_2/README.md

* lab1_2/main/CMakeLists.txt

* lab1_2/main/main.c

* lab1_3/sdkconfig

* lab1_3/CMakeLists.txt

* lab1_3/README.md

* lab1_3/main/CMakeLists.txt

* lab1_3/main/main.c

  

The README.md documents should include any issues (like what is not working)

that you may have. If everything works, just write "everything works"

inside the README.md.

  

There should also be a SINGLE PDF file named `"report.pdf"` that includes:

  

* Any question/answer to GPT or equivalent LLM that you used

+ Include the PDF of the chat + the "Share"

* Any google search/code/repo that you used

+ No reddit/stack overflow/....

+ If you use a specific repo as a result from search, cut

and paste the URL

+ You can **ONLY use open-source repositories that have an APACHE or

a BSD-like license.** It is NOT OK to use GPL or repositories

that do not have any explicit license.

- Using a code repo without keeping a license or using

something like GPL will result in a ZERO grade for the

whole lab.

+ You can NOT use any repo from other UCSC students.

- It will be considered academic integrity (cheating)

+  **You CANNOT share** your query searches. Part of the

class is to learn how to look/find information.

- If you share, it is also considered cheating.
