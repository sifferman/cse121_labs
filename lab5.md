# Lab 5 - Morse Code LED

Due Date: Wed 11/20/2024

This lab is about creating some "LED" communication between the PI4 and the
ESP32 board.

## Lab5.1: Morse LED in PI4 (7 points)

Connect the PI4 with an LED.

WARNING: If you miss the resistor, the LED may burn out.

The resistor limits the current to the LED when emitting light. This means that
the lower the resistor, the higher the current. If no resistor is used, it can
burn the LED. I suggest something around 330 Ohm.

The PI4 should be able to transmit any message with the LED in Morse code. It
should be able to send a message in the command line in PI4, and it should show
in Morse code at the LED.  The first argument in the command is the number of
times to send the message. E.g:

```bash
./send 4 "hello ESP32"
```

will toggle the LED with the message "hello ESP32" 4 times. In this case:

```
.... . .-.. .-.. --- / . ... .--. ...-- ..---
.... . .-.. .-.. --- / . ... .--. ...-- ..---
.... . .-.. .-.. --- / . ... .--. ...-- ..---
.... . .-.. .-.. --- / . ... .--. ...-- ..---
```

## Lab5.2: Read ESP32 (6 points)

Using an ADC (see class example), communicate the messages from the PI4 morse
code to the ESP32 receiver. The received messages should be printed in the
console (idf.py monitor).

The photodiode (receiver) has to be at least 1mm away from the LED (sender). A
message like "hello ESP32" should take less than 10 seconds to be sent (close
to 1 character/second).

## Lab5.3: Faster speed (7 points)

This is a variation of the 5.2, here the idea is to increase the transmission
speed. You can do digital GPIO (not ADC) and/or change the ADC settings. You
have to increase the speed in the sender and measure up to "what speed" is
working and when it starts to fail.

Part of the work is to find a "sequence" that may fail, and you have to report
"close" speeds that show when it passes and fails. The speed should be reported
in characters per second.

* E.g: it can send 10 characters/second but fails at 12 characters/second.  The
  difference between pass and fail should be less or equal to 25%. To compute the
  difference (max-min)/min.

* E.g: If you report 12 fail, 10 pass means (12-10)/10 or 2/10 or 20% which is
  fine (less than 25%). If you report 15 fail and 10 pass, it is not OK (5/10 or
  50%).

The 5 labs submitted on time with the fastest transmission rate in the class
will get extra credit (1st 10 points, 2nd 8 points, 3rd 6 points, 4th 4
points, 5th 2 points).

## What/How to submit

Same instructions as lab1. Upload the zip with the code and report.pdf to
Gradescope.

Submit the following files and directories:

* lab5_1/send
* lab5_2/*
* lab5_3/*
