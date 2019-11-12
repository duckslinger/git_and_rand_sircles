from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.Qt import Qt
import sys
from Ui import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        uic.loadUi("Ui.ui", self)

        self.pushButton.clicked.connect(self.draw_circle)
        self.show()

    def paintEvent(self, *args, **kwargs):
        qp = QPainter(self)
        qp.setBrush(QBrush(QColor(
            randint(0, 255), randint(0, 255), randint(0, 255))))

        x = randint(100, 700)
        y = randint(100, 550)

        d = randint(0, 100)

        qp.drawEllipse(x, y, d, d)

    def draw_circle(self):
        self.update()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

