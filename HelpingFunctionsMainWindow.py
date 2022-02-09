from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QPushButton, QLabel
from PyQt5 import QtCore, QtGui
import FileWorkingClass as bd



#-------------------------------CONSTANTS-----------------------------------
FONT_FAMILY = "Arial"


#----------------------------FILEWORKER------------------------------
accents_worker = bd.FileWorker('AllAccents.csv', 'HardAccents.csv')
spelling_worker = bd.FileWorker('AllSpelling.csv', 'HardSpelling.csv')



# Returns the smallest vector in main vector
def GetMaximalFromVectors(Objects: tuple):
    maximum = len(Objects[0])
    result = 0
    for element_number in range(len(Objects)):
        if len(Objects[element_number]) > maximum:
            maximum = len(Objects[element_number])
            result = element_number
    return result

# From vectors with QWidgets return Vertical Layout which contains Horizontal Layouts
def CreateVerticalWithHorizontals(*Objects: list):
    result = QVBoxLayout()
    Widget_One, Widget_Two = CreateWidgetWithButtons(0, Objects), CreateWidgetWithButtons(2, Objects)
    result.addWidget(Widget_One)
    result.addWidget(Widget_Two)
    return result

# Create buttons on main screen application
def CreateMainButtonsDesign(text: str):
    button = QPushButton()
    button.setText(text)
    button.setStyleSheet("""
    QPushButton {{
        background-color: #2ea44f;
        color: rgb(255, 255, 255);
        max-width: 400px;
        max-height: 60px;
        min-height: 50px;
        min-width: 250px;
        border-radius: 25px;
        font-size: 20px;
        font-family: {};
    }}
    
    QPushButton:hover {{
        background-color: #2a9c4a;
    }}
    
    QPushButton:pressed {{
        background-color: #2bb351;
    }}
    """.format(FONT_FAMILY))
    return button

# Create test buttons label
def CreateButtonsLabel(type: int):

    # 1 - AllAccents, 2 - HardAccents, 3 - AllSpelling, 4 - HardSpelling
    titles = ["", "В данную тренировку включены \nвсе слова из банка ФИПИ",
              "В данную тренировку включены все слова,\nкоторые вы добавили в личный словарь",
              "В данную тренировку включены все \nсложные случаи орфографии",
              "В данную тренировку включены все слова,\nкоторые вы добавили в личный словарь"]

    label = QLabel()
    label.setText(titles[type])
    label.setStyleSheet("""
    QLabel {{
        color: #837D7D;
        font-family: {};
        font-size: 20px;
        max-height: 75px;
        min-width: 300px;
        max-width: 500px;
    }}
    """.format(FONT_FAMILY))
    return label

#
def CreateLayoutForMethod(obj1: QWidget, obj2: QWidget):
    layout = QHBoxLayout()
    layout.addWidget(obj1, alignment=QtCore.Qt.AlignLeft)
    layout.addWidget(obj2, alignment=QtCore.Qt.AlignLeft)
    layout.setAlignment(QtCore.Qt.AlignLeft)
    return layout

# Create title label
def CreateHeaderTitleLabel(title):
    label = QLabel()
    label.setText(title)
    label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    label.setStyleSheet("""
    QLabel {{
        font-size: 25px;
        font-family: {};
        max-height: 80%;
        color: rgb(255, 255, 255);
    }}
    """.format(FONT_FAMILY))
    return label

def CreateButtonTitleLabel(text: str):
    label = QLabel()
    label.setText(text)
    label.setStyleSheet("""
    QLabel {{
        max-width: 300px;
        font-size: 25px;
        font-family: {};
    }}
    """.format(FONT_FAMILY))
    return label

def CreateWidgetWithButtons(number: int, objects: tuple):
    Widget = QWidget()

    Main = QVBoxLayout(Widget)
    Main.setSpacing(50)
    Main.setAlignment(QtCore.Qt.AlignVCenter)

    l1 = QVBoxLayout()

    if number == 0:
        l1.addWidget(objects[2][0], alignment=QtCore.Qt.AlignLeft)
    else:
        l1.addWidget(objects[2][1], alignment=QtCore.Qt.AlignLeft)

    l2 = CreateLayoutForMethod(objects[0][number], objects[1][number])
    l3 = CreateLayoutForMethod(objects[0][number + 1], objects[1][number + 1])

    Main.addLayout(l1)
    Main.addLayout(l2)
    Main.addLayout(l3)

    return Widget

def CreateHeaderWidget():
    header = QWidget()
    header.setStyleSheet("""
    QWidget {
        background-color: #24292e;
        max-height: 80px;
    }
    """)
    return header

def CreateButtonsWidget():
    buttons_widget = QWidget()
    buttons_widget.setStyleSheet("""
    QWidget {
        margin-right: 0px;
        min-width: 760px;
    }
    """)

    return buttons_widget

def CreateMainWindowHeader(window, image_path: str, title: str):
    label = CreateHeaderLabel(image_path)
    window.label_text = CreateHeaderTitleLabel(title)
    button_statistic = CreateStaticticButton()
    window.window_header_layout.addWidget(label)
    window.window_header_layout.addWidget(window.label_text)
    window.window_header_layout.addWidget(button_statistic)

def CreateStaticticButton():
    button = QPushButton()
    button.setText("Ваша статистика")
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
        min-width: 200px;
        border-radius: 25px;
    }}
    
    QPushButton:hover {{
        background-color: #2a9c4a;
    }}
    
    QPushButton:pressed {{
        background-color: #2bb351;
    }}
    """.format(FONT_FAMILY))
    return button

def CreateHeaderLabel(path: str):
    label = QLabel()
    pixmap = QtGui.QPixmap('header1.png')
    label.setPixmap(pixmap)
    label.setStyleSheet("""
    QLabel {
        max-height: 50px;
        max-width: 50px;
    }
    """)
    return label

def CreateInfoWidget():
    widget = QWidget()
    widget.setStyleSheet("""
    QWidget {
        margin-left: 0px;
        max-width: 550px;
    }
    """)
    return widget

def CreateBodyWidget():
    widget = QWidget()
    widget.setStyleSheet("""
        QWidget {
            margin-left: 10px;
            margin-right: 10px;
        }
        """)

    return widget

def AddBorderToInfo(layout):
    border = QWidget()
    border.setStyleSheet("""
        QWidget {
            margin-left: 0px;
            max-width: 15px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(255, 255, 255, 255), 
            stop:0.5 rgba(202, 202, 202, 255), stop:1 rgba(255, 255, 255, 255));
        }
        """)
    layout.addWidget(border, QtCore.Qt.AlignLeft)

def AddInfoToInfo(layout, window):
    info = CreateInfoLayout(window)
    layout.addLayout(info)

def CreateLabelForInfo(text):
    label = QLabel()
    label.setText(text)
    label.setStyleSheet("""
    QLabel {{
        color: #000000;
        font-size: 20px;
        font-family: {};
        font-style: bold;   
    }}
    """.format(FONT_FAMILY))
    return label

def CreateInfoLayout(window):
    result = QVBoxLayout()
    vector_numbers = GetVectorCountsWords()
    vector_labels = ["Весь словарь\nударений составляет: ", "Сложных ударений: ", "Весь словарь\nорфографии составляет: ",
                    "Сложная орфография: "]
    window.vector_numbers = vector_numbers
    result.addWidget(CreateTitleLabelInfo())
    for i in range(len(vector_labels)):
        text = vector_labels[i] + str(vector_numbers[i])
        label = CreateLabelForInfo(text)
        result.addWidget(label)
    return result

def GetVectorCountsWords():
    global accents_worker, spelling_worker
    vector = [0] * 4
    vector[0] = len(accents_worker.get_words('all'))
    vector[1] = len(accents_worker.get_words('hard'))
    vector[2] = len(spelling_worker.get_words('all'))
    vector[3] = len(spelling_worker.get_words('hard'))
    return vector

def CreateTitleLabelInfo():
    label = QLabel()
    label.setText("СЛОВАРИ")
    label.setStyleSheet("""
    QLabel {{
        color: #000000;
        font-family: {};
        font-size: 40px;
        font-style: bold;
    }}
    """.format(FONT_FAMILY))
    return label

