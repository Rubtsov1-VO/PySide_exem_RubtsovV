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
import sys
import datetime
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QPlainTextEdit, QSpinBox
from PyQt6.QtCore import QTimer



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расширенное окно PyQt")


        self.plain_text_edit = QPlainTextEdit()
        self.x_spinbox = QSpinBox()
        self.y_spinbox = QSpinBox()
        self.x_spinbox.setRange(-10000, 10000)  # Устанавливаем большой диапазон, чтобы вместить любые координаты
        self.y_spinbox.setRange(-10000, 10000)
        self.move_button = QPushButton("Переместить окно")


        main_layout = QVBoxLayout()
        main_layout.addWidget(QtWidgets.QLabel("X Координата:"))
        main_layout.addWidget(self.x_spinbox)
        main_layout.addWidget(QtWidgets.QLabel("Y Координата:"))
        main_layout.addWidget(self.y_spinbox)
        main_layout.addWidget(self.move_button)
        main_layout.addWidget(self.plain_text_edit)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


        self.move_button.clicked.connect(self.move_window_to_coordinates)

        self.update_screen_info()


        self.old_pos = self.pos()


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_screen_info)
        self.timer.start(10000)

    def move_window_to_coordinates(self):
        x = self.x_spinbox.value()
        y = self.y_spinbox.value()
        self.move(x, y)
        self.update_screen_info()

    def update_screen_info(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = f"{timestamp}: Обновление информации об экране\n"

        screens = QtWidgets.QApplication.screens()
        output += f"  - Количество экранов: {len(screens)}\n"

        primary_screen = QtWidgets.QApplication.primaryScreen()
        output += f"  - Текущий основной экран: {primary_screen.name()}\n"

        screen = QtWidgets.QApplication.screenAt(self.pos())
        if screen:
            output += f"  - Разрешение экрана: {screen.geometry().width()}x{screen.geometry().height()}\n"
            output += f"  - Окно находится на экране: {screen.name()}\n"
        else:
            output += "  - Окно не находится ни на одном экране\n"

        output += f"  - Размеры окна: {self.width()}x{self.height()}\n"
        output += f"  - Минимальные размеры окна: {self.minimumWidth()}x{self.minimumHeight()}\n"
        output += f"  - Текущее положение (координаты) окна: {self.x()}, {self.y()}\n"

        center = self.geometry().center()  # Геометрия окна
        output += f"  - Координаты центра приложения: {center.x()}, {center.y()}\n"

        if self.isMinimized():
            output += "  - Состояние окна: Свернуто\n" + timestamp
        elif self.isMaximized():
            output += "  - Состояние окна: Развернуто\n" + timestamp
        elif self.isActiveWindow():
            output += "  - Состояние окна: Активно\n" + timestamp
        elif self.isVisible():
            output += "  - Состояние окна: Отображено\n" + timestamp
        else:
            output += "  - Состояние окна: Неизвестно\n" + timestamp

        self.plain_text_edit.appendPlainText(output)
        self.plain_text_edit.ensureCursorVisible()

    def moveEvent(self, event):

        new_pos = self.pos()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp}: Окно перемещено из {self.old_pos.x()}, {self.old_pos.y()} в {new_pos.x()}, {new_pos.y()}")
        self.old_pos = new_pos

    def resizeEvent(self, event):
        new_size = self.size()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp}: Размер окна изменен на {new_size.width()}x{new_size.height()}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




