# infopanel
Always-on panel showing weather, news, webcam feeds and calendar

## Build package
Edit the following files providing the required data:
* /var/www/html/index.html
    * <WEATHERSTATION_URL> = URL to PI based weatherstation (see https://www.youtube.com/playlist?list=PL-Og3KJkUZIndegOxIO6h-F4gTCgepkS8)
    * <WEBCAMS_URL> = URL to HTML page that renders your webcam(s)
* /var/www/html/calendar
    * <CALENDAR_URL> = embed URL for your Google Calendar (go to https://calendar.google.com, click settings, select the calendar you wish to use, click Integrate Calendar and copy the URL listed under 'Embed code')

Then build the package with:
```
dpkg-deb -b infopanel
dpkg-name infopanel.deb
```

## Install package
```
apt install ./infopanel_1.0.0_arm64.deb
```
Restart Apache once it's installed:
```
systemctl restart apache2
```

