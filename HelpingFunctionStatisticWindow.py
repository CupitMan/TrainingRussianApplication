from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QPushButton, QLabel, QInputDialog
from PyQt5 import QtCore, QtGui
import FileWorkingClass as bd
from HelpingFunctionsMainWindow import *

#-------------------------------CONSTANTS-----------------------------------
FONT_FAMILY = "Arial"


class ButtonsWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('''
        QWidget {{
            min-width: 100px;
            min-height: 60px;
            max-height: 80px;
            font-family: {};
            background-color: #4502FF;
        }}
        '''.format(FONT_FAMILY))