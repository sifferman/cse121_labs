# Lab 1 - Lab Setup and trivial tests

Due Date: Tues 10/15/2024

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
(not the Pi4 default).    This can be sufficient to complete
the lab.  We will also install X-Windows an XFACE desktop
which adds extra user friendly functionality.

1. Place the Pi4 into its case. Ground yourself when
   handling this card so as to avoid possible failure due
   to static electricity.  The Pi4 is the most expensive
   card in your kit, the case will protect the device.
   Protecting electronics against static electricity is always
   a good idea.  Note that this is a very nice case.
   The Pi4's CPU will be in contact with a thermal contact
   which eliminates the need for a fan.

2. Install a the Pi Imager software into a host computer, so
   that we can flash the Operating System into the Pi4 microSD.
   Details for downloading Pi Imager for various computer
   platforms (Mac, Windows or Linux) can be found here:
      https://www.raspberrypi.com/software/

3. In order to flash the microSD insert it into the CanaKit
   "USB MicroSD Card Reader" device.

4. Download the UBUNTU 64-bit server image (not the default one)
   (https://ubuntu.com/download/raspberry-pi)

5. Insert MicroSD Card Reader into a USB Port in the computer.
   Start the raspberry-pi imager in order to Flash the microSD
   BEWARE!! Be very careful that you choose the right destination
   (e.g. the correct 128GB USB based storage) and not any other
   drive in your computer, or you will be EXTREMELY sorry you
   did not heed  this advice!  Click on the gear and do your best
   with the settings for installing the software.

5. Extract the microSD from the USB MicroSD Card Reader and
   insert it back into the Pi4 box microSD slot.
   Connect cables for keyboard, monitor, and mouse.
   Power on the device, and allow it to boot. Then type this
   to login (unless you changed user name and passwd in the settings):

   login: ubuntu
   password: ubuntu

   NOTE: if you might also be able a serial port to connect to the
   PI4 UART and a terminal for this part of the setup,
   but we reccommend use of a monitor with an HDMI interface.

6. If you do an `ls` and find that some colors are unreadable, such
   as for directories, you may want to add a file in your home
   direcory called .dircolors with an entry such as:

      DIR 01;36 # teal color for directories

   After you start a new shell you might see color changes when you
   do `ls`.  If you want to change other colors, read more about
   LSCOLORS and dircolors.

7. Setup Wifi

   This is a bit trickier because the default ubuntu server does
   not install the required commands to run eduroam.

   Therefore you must either (option 1) connect to the ethernet port
   OR (option 2) use a non-eduroam way to connect with WiFi.

   Option 2: (not using school eduroam, but home wireless) See:
   > https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line

   Option 3: Use an ethernet cable connected to your router at home or
   configure the Pi4 to use your own WiFi.

   Option 4: Use a phone hotspot.

   You will need Eudoroam to access the Internet in our Lab room.

8. Upgrade ubuntu and install required packages

   ```bash
   sudo apt update
   sudo apt upgrade
   ```

9. Install XFCE window manager.

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
   crash.  A good tool to look at the memory and other resources that
   you are using is called: htop.

   You can complete the rest of this lab, using the command line,
   or X-Windows.

7. Connect/setup to eduroam (AND INCLUDE IT in report.pdf)

   To connect to eduroam, you must install the **nmcli** (there may
   be other options which are OK if you get it working). Notice nmcli
   is not installed by default. You may need a wired or open wifi (step 5).

   ```bash
   sudo apt install network-manager

   nmcli con add type wifi con-name "eduroam" \
      ifname wlan0 ssid "eduroam" wifi-sec.key-mgmt

   wpa-eap 802-1x.identity "XXX@ucsc.edu" 802-1x.password \
      "XXX" 802-1x.system-ca-certs yes \
      802-1x.eap "peap" 802-1x.phase2-auth mschapv2
   nmcli connection up eduroam --ask
   ```

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

   WARNING: This is a TOP OF THE TREE checkout. What this means is
   that the day that you clone the repo, it may (or not) have a BUG
   and thus it may not work. (top of the tree implies that is the
   latest entry in the git repository tree).

   If you end up have difficulties with this or any other parts of this
   lab, you should include this in your report.pdf along with all the
   gorie details.  This code has been known to be quite reliable under
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
   # (to stop monitor ctrl+])
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
that you may have.  If everything works, just write "everything works"
inside the README.md.

There should also be a SINGLE PDF file named report.pdf that includes:

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
