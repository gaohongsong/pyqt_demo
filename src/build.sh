#!/usr/bin/env bash
#"""
## http://legendtkl.com/2015/11/06/pyinstaller/
#"""

#pyinstaller app.py -D -w
#pyinstaller app.py -F -w
rm -rf ./dist/app
pyinstaller app.py -F -w --icon=resources/images/icon1.ico --version-file=version.txt --name=installer