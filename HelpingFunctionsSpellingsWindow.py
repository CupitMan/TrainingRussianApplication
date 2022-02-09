from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QPushButton, QLabel, QInputDialog, QLineEdit, QSizePolicy
from PyQt5 import QtCore, QtGui
import FileWorkingClass as bd
from HelpingFunctionsMainWindow import *
import HelpingFuctionsAccentsWindow as acsupport

#-------------------------------CONSTANTS-----------------------------------
FONT_FAMILY = "Arial"


#----------------------------FILEWORKER------------------------------
accents_worker = bd.FileWorker('AllAccents.csv', 'HardAccents.csv')
spelling_worker = bd.FileWorker('AllSpelling.csv', 'HardSpelling.csv')


def Else(self, IsOkAnswer, check, maximum):
    while IsOkAnswer != True or not (check):
        Information, IsOkAnswer = QInputDialog.getText(self, 'Орфография', 'Введите количество слов: ')
        if IsOkAnswer:
            check = acsupport.Checker(Information, maximum)
            if check:
                self.number_of_tests = int(Information)
                return Information
        else:
            break


def GetWordVectors(word):

    vector = list()

    for symbol in word.word:

        if word.word.index(symbol) != word.spell:

            button = ButtonLetter()

            if symbol == ' ':
                button.ForSpace()

            button.setText(symbol.upper())
            button.setEnabled(False)
            button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            vector.append(button)

        else:
            line = LabelForLetter()
            vector.append(line)

    return vector




class LabelForLetter(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setMaxLength(1)

        self.setStyleSheet('''
        QLineEdit {{
            font-family: {};
            font-size: 30px;
            max-height: 48px;
            max-width: 48px;
            border-radius: 5px;
            background-color: #89BEC6;
            color: white;
        }}
        '''.format(FONT_FAMILY))


    def Right(self, word):

        self.setText(word.word[word.spell].upper())
        self.setStyleSheet('''
                        QLineEdit {{
                            font-family: {};
                            font-size: 30px;
                            max-height: 48px;
                            max-width: 48px;
                            border-radius: 5px;
                            background-color: rgba(0, 0, 0, 0);
                            color: white;
                        }}
                        '''.format(FONT_FAMILY))

    def Wrong(self, word):

        self.setText(word.word[word.spell].upper())
        self.setStyleSheet('''
                        QLineEdit {{
                            font-family: {};
                            font-size: 30px;
                            max-height: 48px;
                            max-width: 48px;
                            border-radius: 5px;
                            background-color: #41B72E;
                            color: white;
                        }}
                        '''.format(FONT_FAMILY))


class ButtonLetter(QPushButton):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QPushButton {{
            background-color: #80B0B7;
            color: white;
            min-height: 48px;
            min-width: 48px;
            font-family: {};
            font-size: 30px;
            border-radius: 10px;
        }}
    
        QPushButton:hover {{
            border: 2px solid #225230;
        }}
    
        QPushButton:disabled {{
            background-color: #80B0B7;
            border-radius: 10px;
        }}
    
        QPushButton:pressed {{
            background-color: #6A9AA0;
        }}
        """.format(FONT_FAMILY))

    def ForSpace(self):
        self.setStyleSheet('''
                QPushButton {{
                    font-family: {};
                    font-size: 30px;
                    max-height: 48px;
                    max-width: 48px;
                    border-radius: 5px;
                    background-color: rgba(0, 0, 0, 0);
                    color: white;
                }}
                '''.format(FONT_FAMILY))






