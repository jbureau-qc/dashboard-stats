
#!/bin/bash

hostname=$(hostname)
IP=$(/sbin/ifconfig wlan0 | grep inet -m1 | awk '{print $2}')
curl --data "hostname=$hostname&ip=$IP" https://business-tools.stingray.com/api/sessions.php
echo ""
