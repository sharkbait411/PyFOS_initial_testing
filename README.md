# PyFOS_initial_testing README

## Purpose

This is an initial login script and grab basic switch information with the PyFOS class on a Brocade Fibre Channel Switch or Director.

## Version
- Python 3.6

## Packages Installed
Package List:
```bazaar
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Package			Version		Latest
-------------------------------------------------
Inject			3.3.1		3.3.2
certifi			2018.4.16	2018.4.16
chardet			3.0.4		3.0.4
colorconsole		0.7.2		0.7.2
idna			2.7		2.7
mock			2.0.0		2.0.0
pbr			4.0.4		4.2.0
pip			9.0.1		18.0
pyfos			1.0.0		1.0.0
requests		2.19.1		2.19.1
setuptools		28.8.0		40.0.0
six			1.11.0		1.11.0
urllib3			1.23		1.23
xmltodict		0.11.0		0.11.0
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
```

## Initial Setup and Build of Python Work
This script was built with the community application "PyCharm". This is a free application that works on Mac OS, Windows, and Linux.

Steps:
- Install PyCharm
- Create new Project in PyCharm
- Open settings, and select project name
  - Then select Project Interpeter
    - If Python 3.6 is not available, do a show all, and either create one, or select from there.
- Install missing packages from interpeter window (seen above)
- download copy of PyFOS_initial_testing
- unpack and validate that "pyfos_testing.py" is in the project folder.
- open "pyfos_testing.py" and validate that all packages show green or unused. (no red... if there is... install that package)
## Ready to debug/Run
