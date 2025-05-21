"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from lab3 import c_weatherapi_widget, b_systeminfo_widget


class MainWindow(QtWidgets.QMainWindow):
    """
    Главное окно, объединяющее два виджета.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Объединенное окно")

        # Создаем виджеты
        self.widget1 = c_weatherapi_widget.MainWindow()
        self.widget2 = b_systeminfo_widget.MainWindow()

        # Создаем главный виджет, который будет содержать оба виджета
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.widget1)
        main_layout.addWidget(self.widget2)
        central_widget.setLayout(main_layout)

        # Устанавливаем центральный виджет для главного окна
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()