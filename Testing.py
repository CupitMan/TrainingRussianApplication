import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QScrollArea
from TestDesign import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore


class MyWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):

        # Делаем само окно
        super().__init__()
        self.setupUi(self)







def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())