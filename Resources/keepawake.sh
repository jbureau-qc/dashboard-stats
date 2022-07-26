#!/bin/bash

export DISPLAY=:0.0
xdotool key "Escape"

value=$(ifconfig wlan0 | grep "inet 10" | wc -l)

if [ $value -lt 1 ]
then
   sudo dhclient wlan0
fi
