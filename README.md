# camera-slider
This repository is used for a raspberry pi-based camera-slider
Development is still ongoing, so further information and a detailed description coming soon!

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

or you bind the ui file by using the **uic.loadUi-Method** of PyQt5. I tested both ways, but I ended up using the second option (see in [cameraslider_design.py](https://github.com/DennisEder/camera-slider/blob/master/application/cameraslider_gui/cameraslider_design.py) under [cameraslider_gui](https://github.com/DennisEder/camera-slider/tree/master/application/cameraslider_gui)). 

### Structure

