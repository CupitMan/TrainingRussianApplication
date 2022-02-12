from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QPushButton, QLabel, QInputDialog
from PyQt5 import QtCore, QtGui
import FileWorkingClass as bd
from HelpingFunctionsMainWindow import *

#-------------------------------CONSTANTS-----------------------------------
FONT_FAMILY = "Arial"


#----------------------------FILEWORKER------------------------------
accents_worker = bd.FileWorker('AllAccents.csv', 'HardAccents.csv')
spelling_worker = bd.FileWorker('AllSpelling.csv', 'HardSpelling.csv')


# Checks correctness of input data
def Checker(text, number):

    if text == '':
        return False

    # Symbols in text shouldn't be alpha
    for symbol in text:
        if not(symbol.isdigit()):
            return False

    # Number should be less or equal number
    num = int(text)
    if number < num:
        return False
    if num <= 1:
        return False
    return True

# Else Branch in Input Dialog
def Else(self, IsOkAnswer, check, maximum):
    while IsOkAnswer != True or not (check):
        Information, IsOkAnswer = QInputDialog.getText(self, 'Ударения', 'Введите количество слов: ')
        if IsOkAnswer:
            check = Checker(Information, maximum)
            if check:
                self.number_of_tests = int(Information)
                return Information
        else:
            break

# Delete All from Layout
def DeleteAll(self):
    for i in reversed(range(self.window_main_layout.count())):
        self.window_main_layout.itemAt(i).widget().deleteLater()

# Create Accents Window Header
def CreateAccentsWindowHeader(window, image_path: str, title: str):
    label = CreateHeaderLabel(image_path)
    label_text = CreateHeaderTitleLabel(title)
    button_return = CreateButtonReturn()
    window.window_header_layout.addWidget(label)
    window.window_header_layout.addWidget(label_text)
    window.window_header_layout.addWidget(button_return)
    button_return.clicked.connect(window.button_return)

def CreateButtonReturn():
    button = QPushButton()
    button.setText("Вернуться на главную")
    button.setStyleSheet("""
        QPushButton {{
            font-family: {};
            font-size: 18px;
            font-style: bold;
            background-color: #2ea44f;
            color: rgb(255, 255, 255);
            max-width: 250px;
            max-height: 55px;
            min-height: 40px;
            min-width: 200px;
            border-radius: 25px;
        }}
        
        QPushButton:hover {{
        background-color: #2a9c4a;
            }}
    
        QPushButton:pressed {{
            background-color: #2bb351;
        }}""".format(FONT_FAMILY))
    return button

def CreateWindowLabelWidget():
    widget = QWidget()
    widget.setStyleSheet('max-height: 200px;')
    return widget

def CreateWindowWordWidget():
    widget = QWidget()
    return widget

def CreateWindowNextWidget():
    widget = QWidget()
    widget.setStyleSheet('background-color: #BAC345;')
    return widget

def CreateWindowBottomWidget():
    widget = QWidget()
    widget.setStyleSheet('max-height: 100px;')
    return widget

def DeleteWidgetFromLayout(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().deleteLater()

def GetVectorPushButtons(word):
    vector = list()
    for symbol in word.name:
        button = CreateButtonForLetters()
        button.setText(symbol.upper())
        vector.append(button)
    return vector

def CreateButtonForLetters():
    button = QPushButton()
    button.setStyleSheet("""
    QPushButton {{
        background-color: #80B0B7;
        color: white;
        min-height: 55px;
        min-width: 55px;
        font-family: {};
        font-size: 40px;
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
    return button

def CreateLabelSelectWord():
    label = QLabel()
    label.setStyleSheet("""
    QLabel {{
        min-height: 80px;
        min-width: 100px;
        color: #837D7D;
        font-family: {};
        font-size: 25px;
    }}
    """.format(FONT_FAMILY))
    label.setText("Поставьте ударение в данном слове,\nкликнув на нужную букву")
    return label

def CreateThreeButtons(color):
    label = QLabel()
    label.setStyleSheet("""
    QLabel {{
        min-height: 25px;
        max-height: 50px;
        min-width: 200px;
        max-width: 300px;
        color: {};
        font-family: {};
        font-size: 25px;
    }}
    """.format(color, FONT_FAMILY))
    return label

def CreateButtonNext():
    button = QPushButton()
    button.setText("Далее")
    button.setStyleSheet("""
        QPushButton {{  
            font-family: {};
            font-size: 20px;
            font-style: bold;
            background-color: #2ea44f;
            color: rgb(255, 255, 255);
            max-width: 250px;
            max-height: 55px;
            min-height: 40px;
            min-width: 250px;
            border-radius: 25px;
        }}

        QPushButton:hover {{
            background-color: #2a9c4a;
        }}

        QPushButton:pressed {{
            background-color: #2bb351;
        }}
        
        QPushButton:disabled {{
            background-color: #52C672;
            color: #ACECC9;
        }}
        """.format(FONT_FAMILY))
    return button

def CreateButtonBottom(text):
    button = QPushButton()
    button.setText(text)
    button.setStyleSheet("""
        QPushButton {{
            font-family: {};
            font-size: 20px;
            font-style: bold;
            background-color: #2ea44f;
            color: rgb(255, 255, 255);
            max-width: 250px;
            max-height: 55px;
            min-height: 40px;
            min-width: 250px;
            border-radius: 25px;
        }}

        QPushButton:hover {{
            background-color: #2a9c4a;
        }}

        QPushButton:pressed {{
            background-color: #2bb351;
        }}
        
        QPushButton:disabled {{
            background-color: #52C672;
            color: #ACECC9;
        }}
        """.format(FONT_FAMILY))
    return button

def ReturnButtonBottom(flag_button):
    if flag_button == 'all':
        button_bottom = CreateButtonBottom("Добавить слово")
    else:
        button_bottom = CreateButtonBottom("Удалить слово")
    return button_bottom
