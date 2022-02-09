import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import JsonWorking
import Statistic


#-------------------------------CONSTANTS-----------------------------------
FONT_FAMILY = "Arial"



class StatisticWidget(QWidget):
    def __init__(self, dictionary, number):
        super().__init__()

        self.setStyleSheet('border-top: 2px solid black; border-bottom: 2px solid black; background-color:#E5E5E5;')

        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)


        self.label_name = LabelName(dictionary)
        self.label_percent = LabelPercent(dictionary)
        self.label_time = LabelTime(dictionary)
        self.label_all = LabelAll(dictionary)
        self.number = LabelNumber(number)

        self.items = {'name': self.label_name.text(), 'percent': self.label_percent.text(),
                      'time': self.label_time.text(), 'all': int(self.label_all.text())}

        labels = [self.number, self.label_name, self.label_percent, self.label_time, self.label_all]

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

        statistic = Statistic.Statistic(dictionary['name'], dictionary['timeStart'], dictionary['timeEnd'],
                                        dictionary['allCount'], dictionary['rightCount'], dictionary['wrongCount'])

        self.setText(str(statistic.PercentsResultTest())+"%")


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

        statistic = Statistic.Statistic(dictionary['name'], dictionary['timeStart'], dictionary['timeEnd'],
                                        dictionary['allCount'], dictionary['rightCount'], dictionary['wrongCount'])

        self.setText(statistic.GetTimeTest())


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

        statistic = Statistic.Statistic(dictionary['name'], dictionary['timeStart'], dictionary['timeEnd'],
                                        dictionary['allCount'], dictionary['rightCount'], dictionary['wrongCount'])

        self.setText(str(statistic.items['allCount']))


class LabelNumber(QLabel):
    def __init__(self, number):
        super().__init__()

        self.setStyleSheet('''
                QLabel {{
                    min-width: 40px;
                    min-height: 50px;
                    max-height: 60px;
                    max-width: 80px;
                    font-family: {};
                    font-size: 30px;
                    color: #837D7D;
                    border-right: 2px solid grey;
                }}
                '''.format(FONT_FAMILY))

        self.setText(str(number))





