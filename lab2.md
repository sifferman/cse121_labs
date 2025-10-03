# Lab 2 - Debugging and Humidity and Temperature

Due Date: Friday 10/17/2025

This lab is worth 20 Points. Project check-off will take place some time after
the lab has been submitted to Gradescope during a future scheduled TA section. The
overall objective of this lab is to use GDB and interface with a RISC-V
executable, and to implement a humidity/temperature sensor.

It is VERY important to submit the **report.pdf** file. If this
file is missing, you lose 1⁄2 of the points.

## Lab2.1: print value with GDB (10 points)

This repo has a "lab2/lab2_debug.elf" file. In order to inspect the contents the elf, we will need to convert to a binary format (.bin):
```bash
esptool.py --chip esp32c3 elf2image <lab2_image.elf>
```
Then flash this file to the esp32c3:
```bash
esptool.py --chip esp32c3 write_flash 0x10000 <lab2_image.bin>
```

Optionally, you can see the full dissasembly of "lab2/lab2_debug.elf" with the following command:

```bash
riscv32-esp-elf-objdump -D lab2/lab2_image.elf > lab2_image.S
```

To demo the first part of lab 2, you'll first flash the board with this bin. Next open the board to be accessed by GDB. Then using GDB, figure out where the `compute` function is called (entry point address), and what values are being input and output(there are 3 values passed to this function, and one value returned).

When the binary runs, it prints something like this (XXX value may change
depending on your board):

```
Minimum free heap size: 286984 bytes
result of compute is XXX
result of compute is XXX
result of compute is XXX
```

To help you a bit, prior to using gdb and flashing your program you will have
to enable the openocd protocol with the command:

```bash
idf.py openocd -f board/esp32c3-builtin.cfg
```

*If you receive this error, perform the following steps.*
```
Error: [esp32c3] Unsupported DTM version: -1
Error: [esp32c3] Could not identify target type.
```
a. Identify which port the board is connected to by typing
```
lsusb
```
b. Provide yourself the correct permissions by typing the following, replacing X with the bus number next to expressif in part a, and Y being the port.
```
sudo chmod 666 /dev/bus/usb/00X/00Y
```


This command installs a client/server interface which allows gdb to communicate
with the board suing the openocd and JTAG protocols via the USB port. To ensure proper configuration, in your project folder, create a new file named gdbinit.

```bash
vim gdbinit
```
With the contents of the file as:

```gdb
target remote :3333
set remote hardware-watchpoint-limit 2
mon reset halt
flushregs
b app_main
c
```

To start gdb using this gdbinit you run this command:

```bash
riscv32-esp-elf-gdb -x gdbinit lab2_image.elf
```

If GDB stalls and openocd crashes with a message like "software core reset", open gdbinit, and remove the line "mon reset halt". 

Ignore when the next step asks you to type this into gdb.

You will need to learn a few gdb commands. For this lab, this guide will be
more than enough for degugging assembly language with gdb:

<https://web.cecs.pdx.edu/~apt/cs491/gdb.pdf>

Gdb also has an excellent help system.

The answer should be written in the report.pdf. It should be something like:
(note these values are wrong).

1. Explain from how you got the answer (justify the
answer, do not just write the correct value).
2. Show how the 3 parameters are passed to the `compute` function, and how its value
gets returned.
3. Show how you got the address of the requested items.

Example:
```
Lab2.1
    Compute 1st argument is 502 and is passed via register ?
    Compute 2nd argument is 303 and is passed via register ?
    Compute 3rd argument is 404 and is passed via register ?
    Return value is 99 and is returned via register ?
    The entry point of the "compute" function is at address 0x????????
```

Some suggestions to get navigate GDB:

* Check the address location (riscv32-esp-elf-objdump -S binary.elf should help).
* Create binary address checkpoint like b *0x4200bbcc" (or the correct address).
* Run usual gdb command and check the register values before starting to execute `compute`.

## Lab2.2: humidity and temperature (10 points)

In a prior lecture we talked about the, SHTC3 temperature and humidity sensor
contained in the ESP32C3 Rust board, and discussed how the I2C protocol for
communicating with this device works.

For this lab, you will have to write a program that reads the temperature and
humidity, and prints the temperature in degrees C and F and a percentage for
the humidity once every 2 seconds. The output will look something like this
(round to nearest value):

```
Temperature is 20C (or 68F) with a 40% humidity
Temperature is 22C (or 72F) with a 42% humidity
Temperature is 20C (or 68F) with a 44% humidity
...
```

Some special requirements:

* You should use the power up and power down between reads (In class, we did
  not do power down). The power up should be called at most once every 2 seconds.

* You should have a different function for temperature and humidity. Each
  should read at most 3 bytes

* Use the checksum value to check the read results

## What/How to submit

Same instructions as lab1. Upload the zip with the code but without the build
subdirectory and a report.pdf to Gradescope.

Submit the following code files:

* lab2_2/sdkconfig
* lab2_2/CMakeLists.txt
* lab2_2/README.md
* lab2_2/main/CMakeLists.txt
* lab2_2/main/*.c
* lab2_2/main/*.h
