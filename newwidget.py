import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore


class NewWidget(QWidget):
    def __init__(self):
        super().__init__()

        #self.setStyleSheet('max-height: 200px; color: black')
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        #layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet('QPushButton {background-color: #AA8899; min-height: 20px; min-width: 100px;}')
        self.r1 = QPushButton()
        self.r2 = QPushButton()
        self.r3 = QPushButton()
        self.r1.setText('123')
        self.r2.setText('123')
        self.r3.setText('123')
        layout.addWidget(self.r1)
        layout.addWidget(self.r2)
        layout.addWidget(self.r3)


