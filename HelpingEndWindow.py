from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QPushButton, QLabel, QInputDialog, QSizePolicy, QGridLayout
from PyQt5 import QtCore, QtGui
import FileWorkingClass as bd
from HelpingFunctionsMainWindow import *

FONT_FAMILY = "Arial"
SIZE_PERCENT = '160px'


class WidgetLabelResult(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('min-height: 100px; margin: 0px; font-size: 20px;')


class WidgetPercentsResult(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setStyleSheet('margin: 0px; min-height: 100px; margin: 0px;')





class WidgetThreeLabelsResult(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout(self)
        self.layout.setSpacing(20)
        self.layout.setAlignment(QtCore.Qt.AlignBottom)
        self.setStyleSheet('min-height: 100px; margin: 0px;')

    def CreateLayouts(self, vector):


        self.layout.addWidget(vector[0], 0, 0)


        more_information = vector[2]
        more_information.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(more_information, 0, 2, QtCore.Qt.AlignRight)

        self.layout.addWidget(vector[1], 1, 0)
        self.layout.addWidget(StatisticButton(), 1, 2)
        self.layout.addWidget(LineWidget(), 0, 1, 2, 1)
        self.layout.setSpacing(5)








class PercentsLabel(QLabel):
    def __init__(self):
        super().__init__()

    def RedState(self):

        self.setStyleSheet("""
        QLabel {{
            font-size: {};
            min-width: 100px;
            max-width: 450px;
            color: #7C4747;
            font-family: {};
        }}
        """.format(SIZE_PERCENT, FONT_FAMILY))

    def YellowState(self):

        self.setStyleSheet("""
        QLabel {{
                font-size: {};
                min-width: 100px;
                max-width: 450px;
                color: #CDC477;
                font-family: {};
        }}
                """.format(SIZE_PERCENT, FONT_FAMILY))

    def GreenState(self):

        self.setStyleSheet("""
        QLabel {{
                        font-size: {};
                        min-width: 100px;
                        max-width: 450px;
                        color: #87AF46;
                        font-family: {};
        }}
                        """.format(SIZE_PERCENT, FONT_FAMILY))

    def GiveText(self, number):
        if number <= 40:
            self.RedState()
            self.setText(str(number) + "%")
        elif 40 < number < 70:
            self.YellowState()
            self.setText(str(number) + "%")
        else:
            self.GreenState()
            self.setText(str(number) + "%")




class ResultLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QLabel {{
            color: #564B4B;
            font-size: 80px;
            font-family: {};
        }}
        """.format(FONT_FAMILY))\


class InformationLabelLeft(QLabel):
    def __init__(self, text):
        super().__init__()

        self.setText(text)


        self.setStyleSheet("""
                min-width: 400px;
                font-size: 25px;
                max-height 100px;
                font-family: {};
                """.format(FONT_FAMILY))



class StatisticButton(QPushButton):
    def __init__(self):
        super().__init__()


        self.setText("Ваша статистика")
        self.setStyleSheet("""
        QPushButton {{
            font-family: {};
            font-size: 25px;
            font-style: bold;
            background-color: #2ea44f;
            color: rgb(255, 255, 255);
            max-width: 400px;
            max-height: 70px;
            min-height: 70px;
            min-width: 300px;
            border-radius: 25px;
        }}
        
        QPushButton:hover {{
            background-color: #2a9c4a;
        }}

        QPushButton:pressed {{
            background-color: #2bb351;
        }}
        """.format(FONT_FAMILY))


def LineWidget():

    widget = QWidget()
    widget.setStyleSheet('''QWidget { 
        min-height: 40px;
        max-width: 20px;
    }''')
    return widget


#qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255))