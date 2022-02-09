import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import JsonWorking


#-------------------------------CONSTANTS-----------------------------------
FONT_FAMILY = "Arial"



class StatisticWidget(QWidget):
    def __init__(self, dictionary):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.label_name = LabelName(dictionary)
        self.label_percent = LabelPercent(dictionary)
        self.label_time = LabelTime(dictionary)
        self.label_all = LabelAll(dictionary)

        labels = [self.label_name, self.label_percent, self.label_time, self.label_all]

        for label in labels:
            self.layout.addWidget(label)


class LabelName(QLabel):
    def __init__(self, dictionary):
        super().__init__()

        self.setStyleSheet('''
        QLabel {{
            min-width: 150px;
            min-height: 50px;
            max-height: 60px;
            font-family: {};
            font-size: 18px;
        }}
        '''.format(FONT_FAMILY))

        self.setText(dictionary['name'])


class LabelPercent(QLabel):
    def __init__(self, dictionary):
        super().__init__()

        self.setStyleSheet('''
                QLabel {{
                    min-width: 80px;
                    min-height: 50px;
                    max-height: 60px;
                    font-family: {};
                    font-size: 18px;
                }}
                '''.format(FONT_FAMILY))

        self.setText(dictionary['percent'])


class LabelTime(QLabel):
    def __init__(self, dictionary):
        super().__init__()

        self.setStyleSheet('''
                QLabel {{
                    min-width: 80px;
                    min-height: 50px;
                    max-height: 60px;
                    font-family: {};
                    font-size: 18px;
                }}
                '''.format(FONT_FAMILY))

        self.setText(dictionary['time'])


class LabelAll(QLabel):
    def __init__(self, dictionary):
        super().__init__()

        self.setStyleSheet('''
                QLabel {{
                    min-width: 80px;
                    min-height: 50px;
                    max-height: 60px;
                    max-width: 150px;
                    font-family: {};
                    font-size: 18px;
                }}
                '''.format(FONT_FAMILY))

        self.setText(str(dictionary['all']))






