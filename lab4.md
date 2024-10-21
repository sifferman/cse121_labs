# Lab 4 - Create a BlueTooth Mouse

Due Date: Tues 11/12/2024

This lab is worth 20 Points. The overall objective of this task is to use the
ICM-42670-P on the RUST ESP32C3 board as a Bluetooth mouse.  Each time the
board tilts, it should move the mouse in the X/Y direction accordingly. There
are some specific rules on how to control the mouse and the test to pass.

It is VERY important to submit the **report.pdf**. If this file is missing, you
lose 1⁄2 of the points.

## Lab4.1: Board movement (5 points)

Write a program to print in the terminal (must use ESP_LOGI) the UP/DOWN or
LEFT/RIGHT depending on the board inclination.

Since there can be more than one direction, Two words may be printed. E.g: If
the board is inclined UP and LEFT, it should print "UP LEFT".

## Lab4.2: Move mouse left/right (5 points)

This lab requires you to reproduce most of the class Bluetooth project but
instead of showing the volume up/down, it should move the mouse left to right
on the screen, then pause for 5 seconds.

You have to demonstrate during checkout that it connects to the raspberry pi
and that it moves.

## Lab4.3: Integrate (10 points)

Integrate labs 4.1 and 4.2 so that the board inclination controls the mouse
with some extensions. To control the speed of the mouse movement, the
inclination level should be considered with at least 2 levels
(A_BIT_LEFT...A_LOT_LEFT).

There should be some "acceleration" (linear or non-linear). You could look at
the "inclination" level or "speed" to decide the acceleration control.

Additionally, you can also use the time inclined like this for the X-axes when
inclined left:

```c
total_x_delta = a*x_delta;
```

The first time that LEFT is found a=1, if 10ms later still set, a=2, if 50ms
still set a=3.

The idea is that you find some values that make your movement controllable. The
x_delta depends if it is A_BIT_LEFT or A_LOT_LEFT.

The TA will move the mouse, and you will need to click something like the "close"
window button using the ESP32 as mouse in less than 4 seconds.

This means that the TA would move the mouse somewhere in the screen, open a
terminal, and you should click to close the terminal in less than 5 seconds
using the ESP32 board. You have 3 tries, if you need more, you loose 1 point for
each additional.

## What/How to submit

Same instructions as lab1. Upload the zip with the code and report.pdf to Gradescope.

Submit the following directories:

* lab4_1/*
* lab4_2/*
* lab4_3/*
