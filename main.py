import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Кружочки')
        self.setGeometry(100, 100, 400, 300)
        self.pushbutton = QPushButton('Нарисовать', self)
        self.pushbutton.resize(100, 30)
        self.pushbutton.move(150, 250)
        self.pushbutton.clicked.connect(self.drawing)
        self.flag = False
        self.coords = []

    def drawing(self):
        self.size = random.randint(10, 50)
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter(self)
            qp.setBrush(self.color)
            x = random.randint(0, self.width() - self.size)
            y = random.randint(0, self.height() - self.size)
            qp.drawEllipse(x, y, self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())