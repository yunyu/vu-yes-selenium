A simple script to automatically enroll in classes for Vanderbilt's YES, saving you precious seconds during course registration period.

[Demo video](https://files.catbox.moe/3rssc4.mp4)

Prerequisites
==

* Python 2.7 with selenium installed (`pip install selenium`)
* [Chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) binary present in path, working Chrome installation (should also work with Firefox)

Usage
==

1) Export `VUNET_ID` and `VUNET_PW` as environment variables for your shell ([bash](http://askubuntu.com/a/58826), [PowerShell](http://serverfault.com/a/514270)). 

2) Run `python submit_enrollment.py Chrome`.
