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

        self.layout = QHBoxLayout(self)

        self.setStyleSheet('''
        QWidget {{
            min-height: 60px;
            max-height: 80px;
            font-family: {};
        }}
        '''.format(FONT_FAMILY))


def GetWidgetsVector(data: list):

    vector = list()

    for i in data:
        label = LabelSort(i)
        b1 = ButtonSort('sortbuttonup.png', 'sortbuttonup1.png', 'sortbuttonup2.png')
        b2 = ButtonSort('sortbuttondown.png', 'sortbuttondown1.png', 'sortbuttondown2.png')
        vector.append(label)
        vector.append(b1)
        vector.append(b2)

    return vector



class ButtonSort(QPushButton):
    def __init__(self, icon_path, icon_path1, icon_path2):
        super().__init__()

        self.setStyleSheet('''
        QPushButton {{
            background-image: url({});
            max-width: 50px;
            min-width: 50px;
            min-height: 50px;
            max-height: 50px;
            font-family: {};
            font-size: 30px;
            border: none;
        }}
        
        QPushButton:hover {{
            background-image: url({});
        }}
        
        QPushButton:pressed {{
            background-image: url({});
        }}
        '''.format(icon_path, FONT_FAMILY, icon_path1, icon_path2))


class LabelSort(QLabel):
    def __init__(self, text):
        super().__init__()

        self.setText(text)
        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.setStyleSheet('''
        QLabel {{
            min-width: 100px;
            min-height: 50px;
            max-height: 100px;
            max-width: 400px;
            font-family: {};
            font-size: 18px;
            color: white;
        }}
        '''.format(FONT_FAMILY))


class ListWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)