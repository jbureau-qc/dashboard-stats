#!/bin/sh

ROOTUID="0"

if [ "$(id -u)" -ne "$ROOTUID" ] ; then
    echo "This script must be executed with root privileges."
    exit 1
fi


echo -ne '                          [0%]\r'
echo "Setting up device..."

sudo apt-get -y install xdotool >> /dev/null
mkdir Dashboard & cd Dashboard

echo -ne '>>>                       [20%]\r'
echo "Getting sources..."

git clone https://github.com/jbureau-qc/dashboard-stats.git
sudo pip install selenium cryptography pyautogui >> /dev/null

echo -ne '>>>>>>>                   [40%]\r'
echo "Installing Chromium..."

sudo dpkg -i Resources/chromium.deb 

echo -ne '>>>>>>>>>>>>>>            [60%]\r'
echo "Password & Shortcuts..."

echo -ne 'Enter password: '
read pw
python ~/Dashboard/DashboardPackage/CryptHandler.py $pw > Resources/password
sudo cp Resources/kiosk.desktop /etc/xdg/autostart/kiosk.desktop
sudo chmod +x Resources/*.sh

echo -ne '>>>>>>>>>>>>>>>>>>>>>>>   [80%]\r'
echo "Setting up crontab and boot config..."

(crontab -l 2>/dev/null; echo "*/5 * * * * bash ~/Dashboard/Resources/keepawake.sh") | crontab -
(crontab -l 2>/dev/null; echo "* * * * * bash ~/Dashboard/Resources/heartbeat.sh") | crontab -
sudo -i
echo "hmdi_mode=34\nsdtv_aspect=3\nsdtv_mode=0" >> /boot/config.txt

echo -ne '>>>>>>>>>>>>>>>>>>>>>>>>>>[100%]\r'
echo -ne '\n'