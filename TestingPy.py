import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QScrollArea, QWidget, QVBoxLayout, QGridLayout, QGroupBox, QCheckBox
from TestDesign import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore





lst = [u"D", u"E", u"EF", u"F", u"FG", u"G", u"H", u"JS", u"J", u"K", u"M", u"P", u"R", u"S", u"T", u"U", u"V", u"X", u"Y", u"Z"]

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        window_width = 1200
        window_height = 600
        self.setFixedSize(window_width, window_height)
        self.initUI()

    def createLayout_group(self, number):
        sgroupbox = QGroupBox("Group{}:".format(number), self)
        layout_groupbox = QVBoxLayout(sgroupbox)
        for i in range(len(lst)):
            item = QCheckBox(lst[i], sgroupbox)
            layout_groupbox.addWidget(item)
        layout_groupbox.addStretch(1)
        return sgroupbox

    def createLayout_Container(self):
        self.scrollarea = QScrollArea(self)
        self.scrollarea.setFixedWidth(250)
        self.scrollarea.setWidgetResizable(True)

        widget = QWidget()
        self.scrollarea.setWidget(widget)
        self.layout_SArea = QVBoxLayout(widget)

        for i in range(5):
            self.layout_SArea.addWidget(self.createLayout_group(i))
        self.layout_SArea.addStretch(1)

    def initUI(self):
        self.createLayout_Container()
        self.layout_All = QVBoxLayout(self)
        self.layout_All.addWidget(self.scrollarea)
        self.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
