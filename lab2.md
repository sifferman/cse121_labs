# Lab 2 - Debugging and Humidity and Temperature

Due Date: Wed 10/23/2024

This lab is worth 20 Points. Project check-off will take place some time after
the lab has been submitted to Gradescope during a future scheduled TA section. The
overall objective of this lab is to use GDB and interface with a RISC-V
executable, and to implement a humidity/temperature sensor.

It is VERY important to submit the **report.pdf** file. If this
file is missing, you lose 1⁄2 of the points.

## Lab2.1: print value with GDB (10 points)

This repo has a "lab2/lab2_debug.elf" file. You
should convert it to a .bin, then upload it to the ESP32 board, then run GDB with it.

You can see the full dissasembly of "lab2/lab2_debug.elf" with the following command:

```bash
riscv64-unknown-elf-objdump -D lab2/lab2_image.elf > lab2_image.S
```

Some things that you will need to "figure out".

* How can I upload an image obtained from someone else (where I do not have the
  source code)? You will not be able to compile it from the source. There are many
  ways to do this.

* How can I use gdb against a binary/image

* The code was compiled without debug info, so you have to look at the assembly
  code.  If you forgot the RISC-V function call convention, the following
  document explains it: <https://riscv.org/wp-content/uploads/2015/01/riscv-calling.pdf>

One word of caution.   Beware with how of the use of idf.py flash since this
command not only tries to flash your program, it also tries to build a new
lab2_debug.elf for you, potentially wiping out your previous one.

What you have to do is to demonstrate during check-off time in the lab that you
are able to run gdb so as to obtain what the values passed to the `compute`
function (there are 3 values passed to this function, and one value returned).
You will also have to show the entry point address of the `compute` function, and
the address of the instruction within that function that returns a value.

When the binary runs, it prints something like this (XXX value may change
depending on your board):

```
Minimum free heap size: 286984 bytes
result of compute is XXX
result of compute is XXX
result of compute is XXX
```

If the GDB is "unstable". You may need to plug/unplug the board if you see
openocd errors like this:

```
Error: Connect failed. Consider setting up a gdb-attach
```

Or this:

```
Error: failed read at 0x11, status=2
Error: extra data from bitq interface
```

To help you a bit, prior to using gdb and flashing your program you will have
to enable the openocd protocol with the command:

```bash
idf.py openocd
```

This command installs a client/server interface which allows gdb to communicate
with the board suing the openocd and JTAG protocols via the USB port.  To help
make this happen I used this gdbinit file which supplies gdb commands at start
up (others are possible too):

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
riscv-esp32-elf-gdb -x gdbinit build/lab2_debug.elf
```

Note that this cross-compiled gdb is quite finicky.  You may need to run mon
reset halt numerous times to restart the program (don't use the reset buttong
for this purpose); you may also need to use Ctrl-C, and/or unplug and plug the
rust board numerous times, and sometimes you may even need to restart your
computer.

You will need to learn a few gdb commands. For this lab, this guide will be
more than enough for degugging assembly language with gdb:

<https://web.cecs.pdx.edu/~apt/cs491/gdb.pdf>

Gdb also has an excellent help system.

The answer should be written in the report.pdf. It should be something like:
(note these values are wrong). Explain from how you got the answer (justify the
answer, do not just write the correct value).  You will need to be able to show
how the 3 parameters are passed to the `compute` function, and how its value
gets returned, and how you got the address of the requested items.


```
Lab2.1
    Compute 1st argument is 502 and is passed via register ?
    Compute 2nd argument is 303 and is passed via register ?
    Compute 3rd argument is 404 and is passed via register ?
    Return value is 99 and is returned via register ?
    The entry point of the "compute" function is at address 0x????????
```

Some suggestions to get GDB working:

* Get a simple hello world working with GDB and openocd
  * You will see that you need to hit reset and/or flash a few times to work
* Then, overwrite the binary with the class ELF.
  * build and flash again
* The breakpoint command "b app_main", may not work with the new binary (different address maps)
  * Check the address location (riscv32-esp-elf-objdump -S binary.elf should help)
  * Create binary address checkpoint like b *0x4200bbcc" (or the correct address)
* Run usual gdb command and check the register values before starting to execute `compute`

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
