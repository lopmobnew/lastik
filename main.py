import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import *
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        f = open("UI.ui")
        uic.loadUi(f, self)
        f.close()
        self.setWindowTitle('Кружочки')
        self.pushButton.setText('Нарисовать кружочки')
        self.flag = False
        self.pushButton.clicked.connect(self.drawing)
        self.coords = []

    def drawing(self):
        self.size = random.randint(10, 50)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.setBrush(QColor(255, 255, 0))
            x = random.randint(0, self.width() - self.size)
            y = random.randint(0, self.height() - self.size)
            qp.drawEllipse(x, y, self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())