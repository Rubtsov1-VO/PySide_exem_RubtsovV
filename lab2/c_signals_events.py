"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

from PySide6 import QtWidgets, QtGui, QtCore
from ui.c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.screen = QtGui.QGuiApplication.screens()

        print(len(self.ui.screen))



        self.ui.primary = QtGui.QGuiApplication.primaryScreen()
        print(QtGui.QGuiApplication.primaryScreen().size())
        print(QtGui.QGuiApplication.screenAt(self.pos()))
        print(QtGui.QGuiApplication.primaryScreen().physicalSize())
        print(QtGui.QGuiApplication.primaryScreen().virtualSize())



    def event(self, event):
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            self.showWindowChange()
        if event.type() == QtCore.QEvent.Type.ActivationChange:
            self.showWindowChange()
        return super().event(event)





    def showWindowChange(self):
        print(f"Свернуто: {self.isHidden()}")
        print(f"Развернуто: {self.isFullScreen()}")
        print(f"Активно: {self.isActiveWindow()}")
        print(f"Отображено: {self.isVisible()}")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
