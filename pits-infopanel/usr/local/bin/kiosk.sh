#!/bin/bash

xset s noblank
xset s off
xset -dpms
xrandr -o right

cd /home/pi/infopanel/flask
/home/pi/infopanel/flask/venv/bin/python infopanel.py 2>&1 | logger &
CHECK=""
while [ "${CHECK}" != "0" ]
do
	echo "Waiting for application to become available..." | logger
	sleep 1
	wget --spider http://localhost:5000
	CHECK=$?
done

matchbox-window-manager -use_titlebar no &

#chromium --display=:0 --kiosk --incognito --window-position=0,0 http://localhost:5000
epiphany-browser --profile /home/pi/epiphany-profiles http://localhost:5000
#epiphany-browser http://localhost:5000
