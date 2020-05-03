# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from cameraslider_design import cameraslider_design

class cameraslider_gui(QtWidgets.QMainWindow, cameraslider_design):
    def __init__(self, path):
        self.path = path
        super(cameraslider_gui, self).__init__()
        self.setupUI(self.path)

        self.qt_actionConfiguration.triggered.connect(self.switchToConnectionConfiguration)
        self.qt_actionManual.triggered.connect(self.switchToModeManual)
        self.qt_dial_velocity.valueChanged.connect(self.valueChangeManualVelocity)
        self.qt_sl_transPos.valueChanged.connect(self.valueChangeManualTransPos)
        self.qt_dial_rotPos.valueChanged.connect(self.valueChangeManualRotPos)

    def valueChangeManualVelocity(self):
        self.qt_lbl_velocity.setText(str(self.qt_dial_velocity.value()) + ' rpm')

    def valueChangeManualTransPos(self):
        self.qt_lbl_transPosCurrent.setText(str(self.qt_sl_transPos.value()) + ' mm')

    def valueChangeManualRotPos(self):
        self.qt_lbl_rotPosCurrent.setText(str(self.qt_dial_rotPos.value()) + ' deg')

    def switchToConnectionConfiguration(self):
        self.qt_stackedWidget.setCurrentIndex(0)

    def switchToModeManual(self):
        self.qt_stackedWidget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle('Breeze')
    widget = cameraslider_gui(r'C:\Users\Dennis Eder\Desktop\Dennis\Programmierung\40_Raspberry Pi\00_camera_slider\application\cameraslider_gui')
    widget.show()
    sys.exit(app.exec_())
