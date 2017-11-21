pibakery-scripts
===============
Some scripts to run in [PiBakery](https://github.com/davidferguson/pibakery)
_____________________________________________
# 1- Using
For using this scripts you might:

## 1.1- What you need before using it
You should already have the [PiBakery](https://github.com/davidferguson/pibakery) installed

## 1.2- How to use it
Just *Import* the the file **recipe_example.xml** at your [PiBakery](https://github.com/davidferguson/pibakery) program

## 1.3- It should look like

![Alt text](pics/recipe_example.png?raw=true "PiBakery Example")

## 1.4- Run as *root*
You will have to adjust the option for running the scripts as **root** to change the system

## 1.5- Wi-Fi
Please don't forget to adjust your **Network** name and it's **Pass** and encryption **Type**

# 2- Adjusting the scripts
You can easily adjust the scripts using it's parameters:

## 2.1- timezone.py
This script will setup the timezone for you
_____________________________________________

```
usage: timezone.py [-h] [-v] [-t TIMEZONE]

This is script is to be used over the pibakery to change the default timezone

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increase output verbosity
  -t TIMEZONE, --timezone TIMEZONE
                        The timezone be set('Europe/Amsterdan','Europe/Paris',
                        etc...), default: Europe/Berlin
```

You can take a look at the **/usr/share/zoneinfo/** folder with all the possible options

For example, to use it for *Los Angeles* you have to parse the **US/Pacific** option for the timezone

```
/home/pi/pibakery-scripts/timezone.py -t US/Pacific
```

## 2.2- keyboard-layout.py
_____________________________________________
This script will setup the keyboard-layout for you

```
usage: keyboard-layout.py [-h] [-v] [-k KEYBOARD_LAYOUT]

This is script is to be used over the pibakery to change the default keyboard
layout

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increase output verbosity
  -k KEYBOARD_LAYOUT, --keyboard-layout KEYBOARD_LAYOUT
                        The keyboard layout to be set('us','fr', etc...),
                        default: de
```
For example, to use it for *American English* keyboard, you have to parse the **us** option for the keyboard-layout

```
/home/pi/pibakery-scripts/keyboard-layout.py -k us
```

## 3- What else?
Just add your extras that you want to use in your *recipe*

Don't forget to have fun with your Pi
