# infopanel
Always-on panel showing weather, news, webcam feeds and calendar

## Build package
Edit the following files providing the required data:
* pits-infopanel/usr/local/infopanel/flask/templates/base.html
    * <WEATHERSTATION_URL> = URL to PI based weatherstation (see https://www.youtube.com/playlist?list=PL-Og3KJkUZIndegOxIO6h-F4gTCgepkS8)
    * <WEBCAMS_URL> = URL to HTML page that renders your webcam(s)
* pits-infopanel/usr/local/infopanel/flask/templates/index.html
    * <URL FROM CALENDER.GOOGLE.COM EMBED INSTRUCTIONS> = embed URL for your Google Calendar (go to https://calendar.google.com, click settings, select the calendar you wish to use, click Integrate Calendar and copy the URL listed under 'Embed code')

Then build the package with:
```
dpkg-deb -b pits-infopanel
dpkg-name pits-infopanel.deb
```

## Install package
```
apt install ./pits-infopanel_2.0.1_arm64.deb
```
Restart Apache once it's installed:
```
systemctl restart apache2
```

