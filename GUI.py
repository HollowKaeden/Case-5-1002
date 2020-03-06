# Интерфейс
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Help')
        self.setWindowIcon(QIcon('web.png'))
        btn = QPushButton('ВыХоД', self)
        btn.clicked.connect(self.hello)
        btn.move(110, 90)
        combo = QComboBox(self)
        combo.addItems(['Алмазный', 'Восточный', 'Западный', 'Курортный', 'Лесной',
                        'Научный', 'Полярный', 'Портовый', 'Приморский', 'Садовый',
                        'Северный', 'Степной', 'Таёжный', 'Центральный', 'Южный'])
        combo1 = QComboBox(self)
        combo1.addItem("Pear")
        combo1.move(110, 0)
        self.show()


    def hello(self):
        plt.plot([1, 2, 3, 4, 5], [1, 3, 1, 3, 1])
        plt.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
