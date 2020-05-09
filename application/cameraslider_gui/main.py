# This Python file uses the following encoding: utf-8
import sys
import os
import time
import threading
from typing import Callable, List, Any, TypeVar

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from cameraslider_design import cameraslider_design

ProgressBar = TypeVar('ProgressBar')

class cameraslider_gui(QtWidgets.QMainWindow, cameraslider_design):
    def __init__(self, path):
        ''' 
        GENERAL
        -------
        Constructor for class cameraslider_gui 
        
        PARAMETER
        ---------
        path    :   str :   entire path is stored in string format

        OUTPUT
        ------
        no output 
        '''
        super(cameraslider_gui, self).__init__()
        # define all class attributes
        self.path: str = path
        self.isConnected: bool = False
        self.progressBar: ProgressBar = QtWidgets.QProgressBar()

        # setup the UI by loading the correspondig ui-file
        self.setupUI(self.path)

        # connect all GUI-Elements to their corresponding functions
        self.qt_actionConfiguration.triggered.connect(self.switchToConnectionConfiguration)
        self.qt_actionConnectDisconnect.triggered.connect(self.connectDisconnectDevice)
        self.qt_actionManual.triggered.connect(self.switchToModeManual)
        self.qt_dial_transVel.valueChanged.connect(self.valueChangeManualTransVel)
        self.qt_dial_rotVel.valueChanged.connect(self.valueChangeManualRotVel)
        self.qt_sl_transPos.valueChanged.connect(self.valueChangeManualTransPos)
        self.qt_sl_rotPos.valueChanged.connect(self.valueChangeManualRotPos)
        self.qt_pb_startSlider.clicked.connect(self.startSliderCurrentSettings)

    def switchToConnectionConfiguration(self):
        '''A custom function which is called when clicking on "Configuration" in MenuBar -> jump
        directly to page "Configuration of stackedWidget'''
        self.qt_stackedWidget.setCurrentIndex(0)

    def switchToModeManual(self):
        '''A custom function which is called when clicking on "Manual" in MenuBar -> jump
        directly to page "Manual" of stackedWidget'''
        self.qt_stackedWidget.setCurrentIndex(1)

    def connectDisconnectDevice(self):
        ''' 
        GENERAL
        -------
        A custom functipn which is called when clicking "Connect" or "Disconnect" in MenuBar ->
        
        PARAMETERS
        ----------
        no parameters

        OUTPUT
        ------
        no output

        '''
        # if-condition: connection not yet established
        if self.isConnected == False:
            # change the stylesheet and the message-text of the statusbar
            self.qt_statusbar.setStyleSheet("QStatusBar{background-color:rgb(0, 170, 0); \
                font: 25 12pt Consolas; color: rgb(30, 39, 46)}")
            self.qt_statusbar.showMessage('connected')
            self.qt_actionConnectDisconnect.setText('Disconnect')
            
            # set the member-variable "isConnected" to true -> connected
            self.isConnected = True

        # elif-condition: connection already established
        elif self.isConnected == True:
            # change the stylesheet of the status bar
            self.qt_statusbar.setStyleSheet("QStatusBar{background-color:rgb(255, 94, 87); \
                font: 25 12pt Consolas; color: rgb(30, 39, 46)}")            
            
            # initialize and start a new thread for adjustments of the status bar
            self.thread = QtCore.QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.worker.statusBarColor.connect(self.resetStatusBarColor)
            self.worker.finished.connect(self.thread.quit)
            self.thread.started.connect(self.worker.resetStatusBarColor)
            self.thread.start()

            # change the message text of the statusbar within the main-thread
            self.qt_statusbar.showMessage('disconnected', 5000)
            self.qt_statusbar.clearMessage()
            self.qt_actionConnectDisconnect.setText('Connect')

            # set the member-variable "isConnected" to false -> no device is connected
            self.isConnected = False

    def valueChangeManualTransVel(self):
        ''' A custom function which is called when the slider for translatory velocity was moved ->
        Current value will be shown in label "qt_lbl_transVelCurrent" '''
        self.qt_lbl_transVelCurrent.setText(str(self.qt_dial_transVel.value()) + ' rpm')

    def valueChangeManualRotVel(self):
        ''' A custom function which is called when the slider for rotatory velocity was moved -> 
        Current value will be shown in label "qt_lbl_rotVelCurrent" '''
        self.qt_lbl_rotVelCurrent.setText(str(self.qt_dial_rotVel.value()) + ' rpm')

    def valueChangeManualTransPos(self):
        ''' A custom function which is called when the slider for translatory position was moved ->
        Current value will be shown in label "qt_lbl_transPosCurrent" '''
        self.qt_lbl_transPosCurrent.setText(str(self.qt_sl_transPos.value()) + ' mm')

    def valueChangeManualRotPos(self):
        ''' A custom function which is called when the slider for rotatory position was moved -> 
        Current value will be shown in label "qt_lbl_rotPosCurrent" '''
        self.qt_lbl_rotPosCurrent.setText(str(self.qt_sl_rotPos.value()) + ' deg')

    def startSliderCurrentSettings(self):
        '''
        GENERAL
        -------
        This function is used for starting the slider in manual mode. In dependence on the member-
        variable "isChecked" the behaviour of the application will be managed.

        PARAMETER
        ---------
        no parameters

        OUTPUT
        no output

        '''
        # if-condition: connection established and push-button no longer/not yet checked
        if self.qt_pb_startSlider.isChecked() == False and self.isConnected == True:
            # change text of the push-button
            self.qt_pb_startSlider.setText('Run')
        
        # elif-condition; connection established and push-button is checked (pressed beforehand)
        elif self.qt_pb_startSlider.isChecked() == True and self.isConnected == True:
            # change text of the push button and initialize the progress-bar
            self.qt_pb_startSlider.setText('Running')
            self.qt_pb_startSlider.setEnabled(False)
            self.progressBar.minimum = 0
            self.progressBar.maximum = 100
            self.progressBar.value = 0
            self.qt_statusbar.addWidget(self.progressBar)
            self.progressBar.show()

            # start a thread for running the slider-function (manuel manoeuvres -> function-class)
            self.thread = QtCore.QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.worker.progressBarValue.connect(self.updateProgressBarValue)
            self.worker.finished.connect(self.thread.quit)
            self.thread.started.connect(self.worker.updateProgressBarValue)
            self.thread.start()

    def resetStatusBarColor(self, newStatusBarColor: str) -> None:
        ''' 
        GENERAL
        -------
        A custom function for resetting the background-color of the statusbar -> called out of 
        a separate track after the entry "Disconnect" in the MenuBar has been pressed" 
        
        PARAMETER
        ---------
        newStatusBarColor   :   str :   background-color in RGB-Format

        OUTPUT
        no output

        '''
        self.qt_statusbar.setStyleSheet('QStatusBar{background-color:' + newStatusBarColor + ';}')

    def updateProgressBarValue(self, progress: int) -> None:
        ''' 
        GENERAL
        -------
        This function is used for updating the progress-bar (member-variable "progressBar")

        PARAMETERS
        ----------
        progress    :   int :   current progress of the corresponding procedure

        OUTPUT
        ------

        '''
        # if-condition: as long as the progress is below 100 %, only the value will be updated
        if progress < 100:
            self.progressBar.setValue(progress)
        # elif-condition: as soon as the procedure is completed, the value will be updated and 
        # some additional changes with respect to the appearence of the gui will be made
        elif progress == 100:
            self.progressBar.setValue(progress)
            self.qt_statusbar.removeWidget(self.progressBar)
            self.qt_pb_startSlider.toggle()
            self.qt_pb_startSlider.setText('Run')
            self.qt_pb_startSlider.setEnabled(True)
        

class Worker(QtCore.QObject):
    finished: Any = QtCore.pyqtSignal()
    statusBarColor: Any = QtCore.pyqtSignal(str)
    progressBarValue: Any = QtCore.pyqtSignal(int)

    @QtCore.pyqtSlot()
    def resetStatusBarColor(self):
        time.sleep(5)
        self.statusBarColor.emit('rgb(30, 39, 46)')
        self.finished.emit()

    @QtCore.pyqtSlot()
    def updateProgressBarValue(self):
        for step in range(1, 101):
            time.sleep(0.1)
            self.progressBarValue.emit(step)
        self.finished.emit()
            


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Breeze')
    widget = cameraslider_gui(r'C:\Users\Dennis Eder\Desktop\Dennis\Programmierung\40_Raspberry Pi\00_camera_slider\camera-slider\application\cameraslider_gui')
    widget.show()
    sys.exit(app.exec_())
