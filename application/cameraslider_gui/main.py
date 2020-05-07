# This Python file uses the following encoding: utf-8
import sys
import os
import time
import threading

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from cameraslider_design import cameraslider_design

class cameraslider_gui(QtWidgets.QMainWindow, cameraslider_design):
    def __init__(self, path):
        self.path = path
        super(cameraslider_gui, self).__init__()
        self.setupUI(self.path)

        self.qt_actionConfiguration.triggered.connect(self.switchToConnectionConfiguration)
        self.qt_actionConnectDisconnect.triggered.connect(self.connectDisconnectDevice)
        self.qt_actionManual.triggered.connect(self.switchToModeManual)


        self.qt_dial_transVel.valueChanged.connect(self.valueChangeManualTransVel)
        self.qt_dial_rotVel.valueChanged.connect(self.valueChangeManualRotVel)
        self.qt_sl_transPos.valueChanged.connect(self.valueChangeManualTransPos)
        self.qt_sl_rotPos.valueChanged.connect(self.valueChangeManualRotPos)
        self.qt_pb_startSlider.clicked.connect(self.startSliderCurrentSettings)

    def switchToConnectionConfiguration(self):
        self.qt_stackedWidget.setCurrentIndex(0)

    def switchToModeManual(self):
        self.qt_stackedWidget.setCurrentIndex(1)

    def connectDisconnectDevice(self):
        if self.qt_actionConnectDisconnect.text() == 'Connect':
            self.qt_statusbar.setStyleSheet("QStatusBar{background-color:rgb(0, 170, 0); font: 25 12pt Consolas; color: rgb(30, 39, 46)}")
            self.qt_statusbar.showMessage('connected')
            self.qt_actionConnectDisconnect.setText('Disconnect')
        elif self.qt_actionConnectDisconnect.text() == 'Disconnect':
            self.colorChanger = myThread()
            self.colorChanger.color.connect(self.changeColorAfterPause)
            self.colorChanger.start()
            self.qt_statusbar.setStyleSheet("QStatusBar{background-color:rgb(255, 94, 87); font: 25 12pt Consolas; color: rgb(30, 39, 46)}")
            self.qt_statusbar.showMessage('disconnected', 5000)
            self.qt_statusbar.clearMessage()
            self.qt_actionConnectDisconnect.setText('Connect')

    def valueChangeManualTransVel(self):
        self.qt_lbl_transVelCurrent.setText(str(self.qt_dial_transVel.value()) + ' rpm')

    def valueChangeManualRotVel(self):
        self.qt_lbl_rotVelCurrent.setText(str(self.qt_dial_rotVel.value()) + ' rpm')

    def valueChangeManualTransPos(self):
        self.qt_lbl_transPosCurrent.setText(str(self.qt_sl_transPos.value()) + ' mm')

    def valueChangeManualRotPos(self):
        self.qt_lbl_rotPosCurrent.setText(str(self.qt_sl_rotPos.value()) + ' deg')

    def startSliderCurrentSettings(self):
        if self.qt_pb_startSlider.isChecked() == True:
            self.qt_pb_startSlider.setText('Stop')
        else:
            self.qt_pb_startSlider.setText('Run')
    
    def changeColorAfterPause(self, value):
        self.qt_statusbar.setStyleSheet("QStatusBar{value}")


class myThread(QtCore.QThread):
    color = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super(myThread, self).__init__()
    
    def run(self):
        time.sleep(5)
        self.color.emit('background-color: rgb(30, 39, 46)')



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Breeze')
    widget = cameraslider_gui(r'C:\Users\Dennis Eder\Desktop\Dennis\Programmierung\40_Raspberry Pi\00_camera_slider\camera-slider\application\cameraslider_gui')
    widget.show()
    sys.exit(app.exec_())
