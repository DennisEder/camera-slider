# Camera-slider with two stepper motors and a Raspberry Pi 3B+
**CAUTION:** Development is still ongoing, so further information and a detailed description coming soon.
If you would like to contribute, just send a pull request!

*********

# General
This repository provides a comprehensive description of my approach building a camera-slider with a Raspberry Pi 3B+ and NEMA17 stepper motors. One the one hand, it should be a kind of a project documentation for myself, one the other hand it can be seen as a step-by-step guide for others, who are also interested in building a camera-slider like this!

## Used components:
* Rapsberry Pi 3B+ 
* 2x NEMA17 - 17HD48002H-22B stepper motor
* 2x TB660 stepper driver (9-42V)
* 12V DC Power supply

********

# Implementation
## Mechanical development
### 3D-Modelling

## Electronical development
### Wiring

## Software development
### Running the stepper motors

## Desktop Application
### General
For the development of the graphical user interface, I utilized the Qt-Framework in combination with PyQt5.
I made this choice primarily because of the huge functionality and its proper documentation. Moreover, it kind of made sense to go with python even for the GUI-Development, due to the fact, that raspberries are basically built for interpreting the python-language. 

The actual design of the app were created with the help of Qt Designer. This is a cost-free tool from Qt, which makes it way more easy setting your layouts or figuring out the position and proportions of relevant widgets. In dependence of your needs and preferences, there are several ways to to integrate your UI-File from Qt Designer in your python code afterwards. Either you translate it directly into a py-file by running the pyuic5.exe of PyQt5 with the following command

**pyuic5.exe -x YOURFILENAME.ui -o YOURFILENAME.py**

or you bind the UI-File by using the 

**uic.loadUi-Method of PyQt5.** 

I tested both ways, but I ended up using the second option (see in [cameraslider_design.py](https://github.com/DennisEder/camera-slider/blob/master/application/cameraslider_gui/cameraslider_design.py) under [cameraslider_gui](https://github.com/DennisEder/camera-slider/tree/master/application/cameraslider_gui)). 

### Structure

