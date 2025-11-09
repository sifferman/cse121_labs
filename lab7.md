# Lab 7 - Weather Station

Due Date: Wednesday 11/26/2025

This lab is worth 20 Points. In this lab, you will use the ESP32 as a weather station that
communicates with a Raspberry Pi server.

The ESP32 will access the internet to query weather (wttr.in) and to ask the server
about the configured location in the weather station.

You may want to watch this video to help you get started: <https://youtu.be/GIbA3fHAHxY>.

## Lab7.1: Get the weather (5 points)

Configure your ESP32 as a network client capable of sending HTTP requests over the internet.
You may connect your ESP32 via any of the following:

* the lab WiFi
* a hotspot through your phone
* a hotspot through your Pi

Get the temperature from wttr.in in celcius.

```
http://wttr.in/:help
```

Check <https://github.com/chubin/wttr.in> for more options

## Lab7.2: Post results (5 points)

Set up a server (on your laptop, phone, or Raspberry Pi) that can receive HTTP requests.
Make sure the server and your ESP32 are connected to the same network.

Your ESP32 should:

1. Read data from its onboard temperature sensor.
2. Send an HTTP POST request to your server on port 1234, containing the temperature reading.

Your server should display or log the information whenever a POST request is received.

## Lab7.3: Integrate both (10 points)

In this part, your will support both GET and POST requests.

1. Modify your server to respond with its current location when it receives the following get request:

    ```
    wget http://SERVER_IP/location
    ```

    (Replace SERVER_IP with your device's actual IP address.)

2. Modify your ESP32 to:

    * Request the server's location.
    * Query wttr.in for the outdoor temperature at that location.
    * Send both the outdoor temperature (from wttr.in) and the sensor temperature
      (from the ESP32) back to the server.

3. Both the server and the ESP32 should log the following information:

    * Server location
    * Outdoor temperature (from wttr.in)
    * ESP32 sensor temperature

## What/How to submit

Same instructions as lab1. Upload the zip with the code and report.pdf to
Gradescope.

Submit the following files and directories:

* lab7_1/*
* lab7_2/*
* lab7_3/*
