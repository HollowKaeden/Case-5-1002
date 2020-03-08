# Интерфейс
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel, QVBoxLayout
import remote as rmt
import dataBase as db


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        db.connect('temp_data_full.db')
        self.setGeometry(300, 300, 370, 220)
        self.setWindowTitle('Программа')
        btn = QPushButton('Получить температуру', self)
        btn.move(110, 90)
        btn.setGeometry(120, 100, 130, 50)
        btn.clicked.connect(self.get_temp)
        self.label_city = QLabel(self)
        self.label_city.setText('Город')
        self.label_city.move(28, 25)
        self.label_areas = QLabel(self)
        self.label_areas.setText('Район')
        self.label_areas.move(140, 25)
        self.label_houses = QLabel(self)
        self.label_houses.setText('Дом')
        self.label_houses.move(235, 25)
        self.label_apartment = QLabel(self)
        self.label_apartment.setText('Квартира')
        self.label_apartment.move(310, 25)
        self.label_get_temp = QLabel(self)
        self.label_get_temp.move(170, 200)
        self.combo_cities = QComboBox(self)
        self.combo_cities.move(0, 40)
        self.combo_cities.addItems([i.name for i in db.get_cities()])
        self.combo_cities.activated[str].connect(self.ccChanged)
        self.combo_areas = QComboBox(self)
        self.combo_areas.move(120, 40)
        self.combo_areas.activated[str].connect(self.caChanged)
        self.combo_houses = QComboBox(self)
        self.combo_houses.move(210, 40)
        self.combo_houses.activated[str].connect(self.chChanged)
        self.combo_apartments = QComboBox(self)
        self.combo_apartments.move(300, 40)
        self.combo_apartments.activated[str].connect(self.capartsChanged)
        self.show()

    def ccChanged(self, text):
        global city_id
        self.combo_areas.clear()
        self.combo_houses.clear()
        self.combo_apartments.clear()
        city_id = db.get_city_id(text)
        self.combo_areas.addItems(list(map(str, range(1, db.get_city_area_count(city_id) + 1))))

    def caChanged(self, text):
        global city_id, area_id
        self.combo_houses.clear()
        self.combo_apartments.clear()
        area_id = int(text)
        self.combo_houses.addItems(list(map(str, range(1, db.get_area_house_count(city_id, area_id) + 1))))

    def chChanged(self, text):
        global city_id, area_id, house_id
        self.combo_apartments.clear()
        house_id = int(text)
        self.combo_apartments.addItems(list(map(str, range(1, db.get_house_apartment_count(city_id, area_id, house_id) + 1))))

    def capartsChanged(self, text):
        global apart_id
        apart_id = int(text)

    def get_temp(self):
        temp = str(rmt.get_apartment_temperature(city_id, area_id, house_id, apart_id))
        print(temp)
        self.label_get_temp.setText('25')
        self.label_get_temp.setText('25')
        # Не могу понять, почему label.get_temp криво изменяется(Осталось только это и 1 задание сделано)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
