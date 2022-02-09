from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from newwidget import NewWidget
from StatisticWidget import StatisticWidget


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        self.central = QtWidgets.QWidget()
        MainWindow.setCentralWidget(self.central)
        self.layout = QtWidgets.QVBoxLayout(self.central)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(QPushButton())

        w = QWidget()
        l = QHBoxLayout(w)
        self.layout.addWidget(w)
        l.setContentsMargins(0, 0, 0, 0)
        l.setSpacing(0)
        mas = [125, 25, 25]
        mas2 = [150, 50, 50]
        for i in range(12):
            if i % 3 == 0 and i != 0:
                l.addSpacing(20)
            self.b1 =QPushButton()
            #max-width: f{mas2[i % 3]}px;
            if i % 3 == 1 or i % 3 == 2:
                self.b1.setStyleSheet(f'min-width: {mas[i % 3]}px; max-width: {mas[i % 3] + 50}px;')
            else:
                self.b1.setStyleSheet(f'min-width: {mas[i % 3]}px;')
            l.addWidget(self.b1)



        list = QListWidget()
        self.layout.addWidget(list)


        for i in range(1000):
            list_item = StatisticWidget({'name': 'Орфография (полностью)', 'percent': '29,67%', 'time': '00:90:89', 'all': 290})
            list_widget_item = QListWidgetItem(list)
            list_widget_item.setSizeHint(list_item.sizeHint())
            list_item.setEnabled(False)
            list_item.setStyleSheet('background-color: #CCD4E4; color: black;')
            list.addItem(list_widget_item)
            list.setItemWidget(list_widget_item, list_item)













        #area.setWidget(widget)



        #self.layout.addWidget(self.button1, QtCore.Qt.AlignBottom)























        #self.widget = QWidget()
        #self.layout.addWidget(self.widget)
        #self.layout1 = QVBoxLayout()
        #self.widget.setLayout(self.layout1)

        #x = [i for i in range(50)]
        #u = []
        #for j in range(50):
            #p = QHBoxLayout()
            #b = QPushButton()
            #k = QPushButton()
            #b.setText(str(j))
            #p.addWidget(b)
            #p.addWidget(k)
            #self.layout1.addLayout(p)

        ##self.widget.setLayout(self.layout1)

        #scroll = QScrollArea()
        #scroll.setWidget(self.widget)
        #self.layout.addWidget(scroll)
        #scroll.setWidgetResizable(True)




