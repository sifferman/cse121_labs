# Lab 1 - Lab Setup and trivial tests

Due Date: Friday 10/10/2025

The overall objective of this lab is to setup the Pi4 (lab1.1),
and program two simple ESP32 programs using the Pi4 board
(lab1.2 and lab1.3). This requires having a WIFI setup (see step 8).

This lab is worth 20 points in total, and is complete when checked-off in lab.
Please ensure your report is uploaded to Lab 1 Report on Gradescope before check-off.
You may demo after the deadline as long as the code is submitted on time.

### What to include in your lab report
1. Screenshot of eduroam connection.
2. How you solved the lab, and difficulties you overcame.
3. Description of AI usage with full chat log.

Please submit your report.pdf to the Lab 1 Report Assignment on Gradescope before your demo.

### Resources

- [Lab 1.2 Example Code](**https://github.com/espressif/esp-idf/blob/master/examples/get-started/hello_world/main/hello_world_main.c**)
- [ESP32-c3 RUST Board Datasheet](**https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf**)

## Lab1.0: Acquire CSE121 Kit (0 points)

You must collect a cse121 kit from BELS' office in JBE-40 (in the basement).
It is yours to borrow for the quarter, then return after finishing the last lab.
If you are missing any parts when you return it, you will have to pay.

## Lab1.1: setup Pi4 (10 points)

Lab1.1 requires you to assemble the components leading to getting
a working Pi4 module and case, functioning with eduroam WiFi and
and linux.

The installation should be based on **ubuntu server**
(not the Pi4 default). This distribution is light weight,
meaning you'll have more RAM. We will also install X-Windows: a
FACE desktop which adds extra user friendly functionality.

1. Place the Pi4 into its case, and avoid removing it,
   as it protects the expensive board from static electricity.
   <br>
2. Install the Pi Imager software onto your personal computer, so
   we can flash the Operating System onto the Pi4 microSD.
   Details for downloading Pi Imager for various computer
   platforms (Mac, Windows or Linux) can be found here:
      <https://www.raspberrypi.com/software/>
   <br>
3. Remove the MicroSD card from the PI4 and insert it into your
   personal computer. If you do not have an adapter, they are
   provided in the red bin in lab.
   <br>
4. Within the imager software (step 2):
   - Under "Raspberry Pi Device" select "Raspberry PI 4"
   - Under "Operating System" select "Other general-purpose OS",
       then select Ubuntu, and finally Ubuntu Server 24.04.3 LTS (64-bit)
   <br>
5. Ensure that your MicroSD card is selected under "Storage".
   The easiest way to confirm is removing it and seeing if it disappears.
   <br>
6. The Imager will prompt you to apply OS customization settings, you can
   type in the local wifi SSID and password in here for convenience sake.
   
   Finally click Yes to erase all existing data on the USB Device and wait
   for the process to complete.
   <br>
7. Extract the microSD from the USB MicroSD Card Reader and
   insert it back into the Pi4 box MicroSD slot. Make the following connections:
   - Keyboard into a USB slot.
   - Display to the PI4 via the HDMI cord using the HDMI 0 slot.
   - AC Adapter into the Canakit PISwitch
   - CanaKit PISwitch into the USB-C port on the PI4.
  
   This will power on the device, and after a few moments, you can
   login using the default username and password:

   ```
   login: ubuntu
   password: ubuntu
   ```
   It will then prompt you to set a new password, choose something memorable!
   <br>

8.  Setup Wifi

   Test if the SSID and password you input in custom OS Settings provides internet
   access by typing

   ```bash
   ping google.com
   ```
   If you see data being retrieved, you can cancel the operation and move onto step 9.

   Otherwise you must manually set the SSID and password until a successful connection.
   See the following resource:
   > <https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line>

   To do so, open the following file like so:
   ```bash
   sudo nano /etc/netplan/50-cloud-init.yaml
   ```
   Confirm that the file is formatted like so, with no tabs, and each indentation being two spaces.
   ```bash
   network:
     version: 2
     wifis:
       wlan0:
         optional: true
         access-points:
             "SSID-NAME-HERE":
               password: "PASSWORD-HERE"
         dhcp4: true
   ```
   Next type the following to apply your changes:
   ```bash
   sudo netplan apply
   ```
   Test your connection by pinging google once more.
   If not, double check for typos or ask a TA for guidance.
   <br>
9. Upgrade ubuntu and install the required packages by typing these two commands.

   ```bash
   sudo apt update
   sudo apt upgrade
   ```
   <br>
10. Install XFCE window manager.

   Perform these steps:

   ```bash
   sudo apt install xfce4 xinit firefox
   ```

   This will help those of you that don't want to make exclusive use
   of the command line interface (CLI).
   You will need to connect a mouse to your Pi4.
   Set it up so that you can start and stop the X-windows interface.

   XFCE is one of several Desktops for X-Windows that is very lightweight
   (uses a small amount of memory).  It is not as lightweight as LXDE,
   but is much more user friendly and easy to install.
   LXDE uses a base of 219 MB RAM, whereas XFCE uses 465 MB RAM.
   You have a total of 4GB of RAM in your Pi4, so you will want to watch
   how much memory you use.  If you use too much memory your Pi4 will
   crash. A good tool to look at the memory and other resources that
   you are using is called: htop.

   You can complete the rest of this lab, using the command line,
   or X-Windows.

   <br>
11. Connect/setup to eduroam (AND INCLUDE IT in report.pdf)

   Once you've installed the XFCE4 window manager, boot into the desktop and you
   can connect to eduroam through the Wifi Manager GUI. Include a screenshot of
   this in your lab report.

## Lab1.2: Run hello world in ESP32 (5 points)

1. Update and upgrade ubuntu and install required packages

   ```bash
   sudo apt update   # synchronizes local directory of the latest packages.
   sudo apt upgrade  # this upgrades packages downloaded to be the latest.

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
   printf("Your Name Here\n"); // Substitute your name
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
   # (to stop monitor ctrl+])
   ```

## Lab1.3: Flash LED on ESP32 (5 Points)

The ESP32C3 board that has a LED connected to GPIO2. Write a simple C program
that flashes the LED on/off once per second.

The app_main should call something like this:

```
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
that you may have.  If everything works, just write "everything works"
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
  + **You CANNOT share** your query searches. Part of the
    class is to learn how to look/find information.
    - If you share, it is also considered cheating.
