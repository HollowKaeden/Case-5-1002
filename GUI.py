# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import remote as rmt
import dataBase as db
import matplotlib.pyplot as plt


class main_window(QWidget):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        self.initUI()

    def initUI(self):
        db.connect()
        font = QFont('Comic sans', 16)
        self.setGeometry(300, 300, 202, 230)
        self.setWindowTitle('Меню')
        self.btn1 = QPushButton('Первое задание', self)
        self.btn1.setFont(font)
        self.btn1.clicked.connect(self.first_task)
        self.btn2 = QPushButton('Второе задание', self)
        self.btn2.setFont(font)
        self.btn2.move(0, 50)
        self.btn2.clicked.connect(self.second_task)
        self.btn3 = QPushButton('Третье задание', self)
        self.btn3.setFont(font)
        self.btn3.move(0, 100)
        self.btn3.clicked.connect(self.third_task)
        self.btn4 = QPushButton('Четвёртое задание', self)
        self.btn4.setFont(font)
        self.btn4.move(0, 150)
        self.btn4.clicked.connect(self.fourth_task)
        self.btn5 = QPushButton('Пятое задание', self)
        self.btn5.setFont(font)
        self.btn5.move(0, 200)
        self.btn5.clicked.connect(self.fifth_task)
        self.show()

    def first_task(self):
        if not self.secondWin:
            self.secondWin = first_task(self)
        self.secondWin.show()

    def second_task(self):
        plt.plot(db.get_cities_temperature_half_year(1))
        plt.ylabel('Температура')
        plt.title('Температура в городе Алмазный')
        plt.show()

    def third_task(self):
        print(db.get_average_temperature(7))

    def fourth_task(self):
        fig, axs = plt.subplots(4, 4)
        plts = list()
        for i in db.get_apartments_temperature_from_all_cities():
            plts.append(list(map(lambda x: float(x[2]), i)))
        for i in range(4):
            for j in range(4):
                if not(i == 3 and j == 3):
                    axs[i, j].plot(plts.pop())
        fig.suptitle('Температура в квартирах')
        plt.show()

    def fifth_task(self):
        pass


class first_task(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.initUI()

    def initUI(self):
        db.connect()
        font = QFont('Times New Roman', 16)
        cfont = QFont('Times New Roman', 13)
        self.setGeometry(300, 300, 393, 220)
        self.setWindowTitle('Программа')
        self.btn = QPushButton('Получить температуру', self)
        self.btn.setFont(font)
        self.btn.setGeometry(90, 100, 210, 50)
        self.btn.clicked.connect(self.get_temp)
        self.btn.setDisabled(True)
        self.label_city = QLabel(self)
        self.label_city.setText('Город')
        self.label_city.setFont(font)
        self.label_city.move(28, 10)
        self.label_areas = QLabel(self)
        self.label_areas.setText('Район')
        self.label_areas.setFont(font)
        self.label_areas.move(144, 10)
        self.label_houses = QLabel(self)
        self.label_houses.setText('Дом')
        self.label_houses.setFont(font)
        self.label_houses.move(243, 10)
        self.label_apartment = QLabel(self)
        self.label_apartment.setText('Квартира')
        self.label_apartment.setFont(font)
        self.label_apartment.move(310, 10)
        self.label_get_temp = QLabel(self)
        self.label_get_temp.move(180, 180)
        self.combo_cities = QComboBox(self)
        self.combo_cities.setFont(cfont)
        self.combo_cities.move(0, 40)
        self.combo_cities.addItems([i.name for i in db.get_cities()])
        self.combo_cities.activated[str].connect(self.ccChanged)
        self.combo_areas = QComboBox(self)
        self.combo_areas.setFont(cfont)
        self.combo_areas.move(130, 40)
        self.combo_areas.activated[str].connect(self.caChanged)
        self.combo_houses = QComboBox(self)
        self.combo_houses.setFont(cfont)
        self.combo_houses.move(220, 40)
        self.combo_houses.activated[str].connect(self.chChanged)
        self.combo_apartments = QComboBox(self)
        self.combo_apartments.setFont(cfont)
        self.combo_apartments.move(310, 40)
        self.combo_apartments.activated[str].connect(self.capartsChanged)
        self.show()

    def ccChanged(self, text):
        global city_id
        self.btn.setDisabled(True)
        self.combo_areas.clear()
        self.combo_houses.clear()
        self.combo_apartments.clear()
        city_id = db.get_city_id(text)
        self.combo_areas.addItems(list(map(str, range(1, db.get_city_area_count(city_id) + 1))))

    def caChanged(self, text):
        global city_id, area_id
        self.btn.setDisabled(True)
        self.combo_houses.clear()
        self.combo_apartments.clear()
        area_id = int(text)
        self.combo_houses.addItems(list(map(str, range(1, db.get_area_house_count(city_id, area_id) + 1))))

    def chChanged(self, text):
        global city_id, area_id, house_id
        self.btn.setDisabled(True)
        self.combo_apartments.clear()
        house_id = int(text)
        self.combo_apartments.addItems(list(map(str, range(1, db.get_house_apartment_count(city_id, area_id, house_id) + 1))))

    def capartsChanged(self, text):
        global apart_id
        self.btn.setDisabled(False)
        apart_id = int(text)

    def get_temp(self):
        temp = str(rmt.get_apartment_temperature(city_id, area_id, house_id, apart_id))
        font = QFont('Arial', 24)
        self.label_get_temp.setFont(font)
        self.label_get_temp.setText(str(temp))
        self.label_get_temp.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_window()
    sys.exit(app.exec_())
