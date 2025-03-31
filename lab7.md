# Lab 7 - Weather Station

Due Date: Wed 5/30/2025

This lab is worth 20 Points. The overall objective of this task is to use the
ESP32 as a weather station that post results in a Raspberry PI server.

The ESP32 will access the internet to query weather (wttr.in) and to ask the server
about the configured location in the weather station.

It is VERY important to submit the **report.pdf**. If this file is missing, you
lose 1⁄2 of the points.

You may want to watch this video to help you get started: <https://youtu.be/GIbA3fHAHxY>.

## Lab7.1: Get the weather (5 points)

This is mostly to reproduce the wttr.in example from class. Check the
SSID/Password and certificate expiration like in class.

### OPTION 1: PI

Similar to class, but you need to setup the PI as a hotspot server. This is
easier if you connect to ethernet (RJ-45) for internet, and use wifi for
hotspot.

### OPTION 2: Phone

In this case, the setup is the same as in the class. But if you pick option 2,
you must also do option 2 (phone) in parts 7.2 and 7.3

Get only the temperature from wttr.in in celcius.

```
https://wttr.in/:help
```

Check <https://github.com/chubin/wttr.in> for more options

## Lab7.2: Post results (5 points)

You must read the humidity and temperature sensor and create an HTTP post
against the IP that provided the hotspot (either phone or PI4) using port 1234.

The ESP32 should send a POST every second to port 1234. The PI (or phone)
should display the information when the post is realized.

## Lab7.3: Integrate both (10 points)

The ESP32 should request the outdoors temperature from wttr.in. The location
should come from the server in the phone (or PI4) using a http (not httpS)

You need to setup a webserver (PI or your phone) that listens to port 1234 to
post temperature+humidity and check the location.

To check the location, this command should run in your PI/Phone (SOME_IP depends on your device)

```
wget http://SOME_IP/location
```

The ESP32 should query the wttr.in with the indicated location, and combine the
information with the local sensors (temperature + humidity) and send it to the
phone (or PI4). The same message should be printed in the log (ESP_LOG) with
the location, wttr.in temperature, and local temperature.

## What/How to submit

Same instructions as lab1. Upload the zip with the code and report.pdf to
Gradescope.

Submit the following files and directories:

* lab7_1/*
* lab7_2/*
* lab7_3/*
