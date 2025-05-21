"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings_form.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QDial, QSlider, QLCDNumber, QComboBox, QLabel)
from PyQt5.QtCore import Qt, QSettings

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.dial = QDial()
        self.slider = QSlider(Qt.Horizontal)
        self.lcd_number = QLCDNumber()
        self.combo_box = QComboBox()

        self.dial.setRange(0, 99)
        self.slider.setRange(0, 99)
        self.lcd_number.setSegmentStyle(QLCDNumber.Flat)

        self.combo_box.addItems(["Dec", "Hex", "Bin", "Oct"])
        self.combo_box.currentIndexChanged.connect(self.update_lcd_display)

        self.settings = QSettings("MyApplication", "LCDSettings")
        self.load_settings()


        self.dial.valueChanged.connect(self.slider.setValue)
        self.dial.valueChanged.connect(self.lcd_number.display)
        self.slider.valueChanged.connect(self.dial.setValue)
        self.slider.valueChanged.connect(self.lcd_number.display)
        self.lcd_number.overflow.connect(self.handle_overflow)


        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel("Dial:"))
        h_layout.addWidget(self.dial)
        h_layout.addWidget(QLabel("Slider:"))
        h_layout.addWidget(self.slider)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(QLabel("LCD Number:"))
        v_layout.addWidget(self.lcd_number)
        v_layout.addWidget(QLabel("Display Mode:"))
        v_layout.addWidget(self.combo_box)

        self.setLayout(v_layout)
        self.dial.setFocusPolicy(Qt.StrongFocus)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self.dial.setValue(min(self.dial.value() + 1, self.dial.maximum()))
            print(f"Dial value increased: {self.dial.value()}")  # Вывод в консоль
        elif event.key() == Qt.Key_Minus:
            self.dial.setValue(max(self.dial.value() - 1, self.dial.minimum()))
            print(f"Dial value decreased: {self.dial.value()}")  # Вывод в консоль
        else:
            super().keyPressEvent(event)

    def update_lcd_display(self, index):
        value = self.lcd_number.value()
        if index == 0:  # Dec
            self.lcd_number.setDecMode()
        elif index == 1:  # Hex
            self.lcd_number.setHexMode()
        elif index == 2:  # Bin
            self.lcd_number.setBinMode()
        elif index == 3:  # Oct
            self.lcd_number.setOctMode()

        self.lcd_number.display(value)

    def load_settings(self):
        display_mode_index = self.settings.value("display_mode", 0, type=int)
        lcd_value = self.settings.value("lcd_value", 0, type=int)

        self.combo_box.setCurrentIndex(display_mode_index)
        self.update_lcd_display(display_mode_index)
        self.dial.setValue(lcd_value)
        self.slider.setValue(lcd_value)
        self.lcd_number.display(lcd_value)

    def save_settings(self):
        self.settings.setValue("display_mode", self.combo_box.currentIndex())
        self.settings.setValue("lcd_value", self.lcd_number.value())

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)

    def handle_overflow(self):
        print("LCD Number Overflow!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())