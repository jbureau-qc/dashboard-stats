#!/bin/bash

cd /home/pi/Dashboard/dashboard-stats/DashboardPackage/

export DISPLAY=:0.0

x11vnc -find -quiet -forever -display :0 -localhost &

value="$(<password)"

while :
do
  pc=$(ps aux | grep chromium | wc -l)
  if [ $pc -lt 6 ]
  then
      python DashboardModule.py $value
  fi
  sleep 10

  ping=$(ping 8.8.8.8 -c 4 | wc -l)
  if [ $ping -lt 4 ]
  then
     sudo reboot
  fi
done
