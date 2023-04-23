from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QSizePolicy
)
from PyQt5.QtGui import QFont

my = QFont('Comic Sans MS', 18)

class StretchButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(40, 40)
        self.setFont(my)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('нормасик лол')

        self.to_slove = ''
        self.display = QLineEdit()

        self.display.setReadOnly(True)
        b0 = StretchButton('0')
        b1 = StretchButton('1')
        b2 = StretchButton('2')
        b3 = StretchButton('3')
        b4 = StretchButton('4')
        b5 = StretchButton('5')
        b6 = StretchButton('6')
        b7 = StretchButton('7')
        b8 = StretchButton('8')
        b9 = StretchButton('9')
        bb = StretchButton('<-')
        bc = StretchButton('C')
        bp = StretchButton('+')
        bm = StretchButton('-')
        b_ = StretchButton('=')
        by = StretchButton('*')
        b = StretchButton('/')
        bt = StretchButton('.')

        l = QGridLayout()
        l.addWidget(self.display, 0, 0, 1, 4)
        l.addWidget(bb, 1, 0)
        l.addWidget(bc, 1, 1)
        l.addWidget(bp, 1, 2)
        l.addWidget(bm, 1, 3)
        l.addWidget(b7, 2, 0)
        l.addWidget(b8, 2, 1)
        l.addWidget(b9, 2, 2)
        l.addWidget(by, 2, 3)
        l.addWidget(b4, 3, 0)
        l.addWidget(b5, 3, 1)
        l.addWidget(b6, 3, 2)
        l.addWidget(b, 3, 3)
        l.addWidget(b1, 4, 0)
        l.addWidget(b2, 4, 1)
        l.addWidget(b3, 4, 2)
        l.addWidget(b_, 4, 3)
        l.addWidget(b0, 5, 1)
        l.addWidget(bt, 5, 2)
        self.setLayout(l)

        b0.clicked.connect(self.btn_hand)
        b1.clicked.connect(self.btn_hand)
        b2.clicked.connect(self.btn_hand)
        b3.clicked.connect(self.btn_hand)
        b4.clicked.connect(self.btn_hand)
        b5.clicked.connect(self.btn_hand)
        b6.clicked.connect(self.btn_hand)
        b7.clicked.connect(self.btn_hand)
        b8.clicked.connect(self.btn_hand)
        b9.clicked.connect(self.btn_hand)
        bb.clicked.connect(self.btn_hand)
        bc.clicked.connect(self.btn_hand)
        bp.clicked.connect(self.btn_hand)
        bm.clicked.connect(self.btn_hand)
        b_.clicked.connect(self.btn_hand)
        by.clicked.connect(self.btn_hand)
        b.clicked.connect(self.btn_hand)
        bt.clicked.connect(self.btn_hand)

    def btn_hand(self):
        btn = self.sender()
        if btn.text() in '0123456789/*-+':
            self.to_slove += btn.text()
        elif btn.text() == '<-':
            self.to_slove = self.to_slove[0:-1]
        elif btn.text() == 'C':
            self.to_slove = ''
        elif btn.text() == '=':
            try:
                self.to_slove = str(eval(self.to_slove))
            except:
                self.to_slove = '0'
        self.display.setText(self.to_slove)
app = QApplication([])
window = MainWindow()
window.show()
app.exec()