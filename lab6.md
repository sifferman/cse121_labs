# Lab 6 - Ultrasonic Range Finder

Due Date: Wed 11/27/2024

This lab is to program the ultrasonic range.

* <https://lastminuteengineers.com/arduino-sr04-ultrasonic-sensor-tutorial>
* <https://media.digikey.com/pdf/Data%20Sheets/Adafruit%20PDFs/4007_Web.pdf>

## Lab6.1: Read distance (20 points)

Use the SR04 to measure the distance, AND also use the temperature sensor to
"adjust" the speed of sound based on the current temperature. Assume that the
temperature is always between 0 and 50C.

The temperature (C) and distance (cm) should be shown in the monitor printed
once per second. E.g:

```
Distance: 3.5 cm at 23C
Distance: 4.5 cm at 23C
```

The distance to measure by the TAs would be from 10 to 20cm. You can calibrate
the sensor, but there should be less than a 2 cm error. The distance is
computed from the PCB board (not the sensor itself) to a flat surface.

NOTE: To get accurate results, you may need to generate multiple pulses, you
may also want to look for counters in the hal/cpu_hal.h that has more
precision.

## What/How to submit

Same instructions as lab1. Upload the zip with the code and report.pdf to
Gradescope.

Submit the following files and directories:

* lab6_1/*
