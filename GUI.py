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

        conn = sqlite3.connect("temp_data_full.db")
        # conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        sql = "SELECT name FROM CITIES"
        cursor.execute(sql)
        self.combo_cities = QComboBox(self)
        self.combo_cities.addItems([i[0] for i in cursor.fetchall()])
        self.combo_cities.activated[str].connect(self.ccChanged)
        self.combo_areas = QComboBox(self)
        self.combo_areas.move(110, 0)
        self.show()


    def ccChanged(self, text):
        cursor = sqlite3.connect("temp_data_full.db").cursor()
        sql = 'SELECT area_count FROM CITIES WHERE name=?'
        cursor.execute(sql, [(text)])
        self.combo_areas.addItems(range(cursor.fetchall()[0][0]))
        self.combo_areas.move(110, 0)

    def hello(self):
        plt.plot([1, 2, 3, 4, 5], [1, 3, 1, 3, 1])
        plt.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
