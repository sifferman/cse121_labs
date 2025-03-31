#!/usr/bin/env bash

# Print Linux Version
lsb_release -a

# Update package list
apt-get update
apt-get upgrade -y
apt-get install -y git wget flex bison gperf \
                   python3 python3-pip python3-dev python3-venv \
                   cmake ninja-build ccache libffi-dev \
                   libssl-dev dfu-util libusb-1.0-0 \
                   gcc build-essential curl pkg-config

# Install python and requirements
pip3 install -r /autograder/source/autograder_requirements.txt

# Install ESP-IDF
mkdir -p /esp
cd /esp
git clone --recursive https://github.com/espressif/esp-idf.git
cd /esp/esp-idf
./install.sh esp32c3
. /esp/esp-idf/export.sh
