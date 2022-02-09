import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindowDesign import MainDesign


class MyApplication(QMainWindow, MainDesign):
    def __init__(self):
        super().__init__()
        self.MainDesign(self)

