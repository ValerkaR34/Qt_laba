from PyQt6 import QtCore, QtWidgets, QtGui
import sys
from ui.create import Ui_MainWindow
import  random

def button_on_off():
    s = ['Ленинград -  Вояж', 'ЛСП - Монетка',  ' Король и шут -Проклятый Старый дом', 'ABBA - Happy new year', 'Mr.Kitty - After Dark', 'Gorillaz - Feel Good Inc.']


    if ui.listWidget.count() == 0:
     for x in s:
        ui.listWidget.addItem(x)
    else:
     ui.listWidget.clear()


def button_random():

        items = [ui.listWidget.item(i).text() for i in range(ui.listWidget.count())] # Cоздал
        # список items, содержащий текст каждого элемента в listWidget. Используется
         # генератор списка для этого. Перебираются все элементы в listWidget и добавляют их текст в список items.

        random.shuffle(items)  # перемешивваем элементы в случайном списке
        ui.listWidget.clear() # очищаем
        for item in items: 
            ui.listWidget.addItem(item)  # добавил каждый элемент из перемешанного списка items в listWidget


if __name__ == "__main__":
    # Создаем приложение
    app = QtWidgets.QApplication(sys.argv)

    # Создаем форму и инициализируем UI
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    # При нажатии на кнопку выполняется её функция
    ui.toolButton.clicked.connect(button_on_off)
    ui.button_rand.clicked.connect(button_random)

    # Запуск
    sys.exit(app.exec())


