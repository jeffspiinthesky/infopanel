#!/bin/bash

xset s noblank
xset s off
xset -dpms
xrandr -o right

cd /usr/local/infopanel/flask
/usr/local/infopanel/flask/venv/bin/python infopanel.py 2>&1 | logger &
CHECK=""
while [ "${CHECK}" != "0" ]
do
	echo "Waiting for application to become available..." | logger
	sleep 1
	wget -O /dev/null --spider http://localhost:5000
	CHECK=$?
done

# matchbox-window-manager -use_titlebar no &

#epiphany --profile=/home/orangepi/.local/share/org.gnome.Epiphany.WebApp_infopanel-7f547fb3955684764fa6453b4951ae984e70ab08 -a infopanel http://localhost:5000 2>&1 | logger &
#firefox-esr --kiosk http://localhost:5000 2>&1 | logger &
chromium-browser --kiosk http://localhost:5000 2>&1 | logger &
sleep 20
xte "key F11" 2>&1 | logger

while [ 1==1 ]
do
	sleep 1
done
