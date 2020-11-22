import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic
from design import Ui_Form


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paint = False
        self.setWindowTitle('Желтые круги')
        self.pushButton.clicked.connect(self.do_paint)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircles(qp)
            qp.end()

    def do_paint(self):
        self.paint = True
        self.repaint()

    def drawCircles(self, qp):
        for i in range(random.randint(1, 10)):
            r, g, b = random.randint(0, 255), random.randint(0, 255), \
                      random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            j = random.randint(20, 100)
            qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), j, j)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

