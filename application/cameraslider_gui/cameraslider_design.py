# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic


class cameraslider_design(object):
    def __init__(self):
        pass

    def setupUI(self, path):
        uic.loadUi(path + r'\application.ui', self)
