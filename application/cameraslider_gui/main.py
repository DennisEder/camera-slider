# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from cameraslider_design import cameraslider_design

# test

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
        self.qt_dial_rotPos.valueChanged.connect(self.valueChangeManualRotPos)
        self.qt_pb_startSlider.clicked.connect(self.startSliderCurrentSettings)

    def switchToConnectionConfiguration(self):
        self.qt_stackedWidget.setCurrentIndex(0)

    def switchToModeManual(self):
        self.qt_stackedWidget.setCurrentIndex(1)

    def connectDisconnectDevice(self):
        self.qt_statusbar.setStyleSheet("QStatusBar{background-color:rgb(0, 170, 0);}")
        self.qt_statusbar.showMessage('connected')
        self.qt_actionConnectDisconnect.setText('Disconnect')


    def valueChangeManualTransVel(self):
        self.qt_lbl_transVelCurrent.setText(str(self.qt_dial_transVel.value()) + ' rpm')

    def valueChangeManualRotVel(self):
        self.qt_lbl_rotVelCurrent.setText(str(self.qt_dial_rotVel.value()) + ' rpm')

    def valueChangeManualTransPos(self):
        self.qt_lbl_transPosCurrent.setText(str(self.qt_sl_transPos.value()) + ' mm')

    def valueChangeManualRotPos(self):
        self.qt_lbl_rotPosCurrent.setText(str(self.qt_dial_rotPos.value()) + ' deg')

    def startSliderCurrentSettings(self):
        if self.qt_pb_startSlider.isChecked() == True:
            self.qt_pb_startSlider.setText('Stop')
        else:
            self.qt_pb_startSlider.setText('Run')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Breeze')
    widget = cameraslider_gui(r'C:\Users\Dennis Eder\Desktop\Dennis\Programmierung\40_Raspberry Pi\00_camera_slider\camera-slider\application\cameraslider_gui')
    widget.show()
    sys.exit(app.exec_())
