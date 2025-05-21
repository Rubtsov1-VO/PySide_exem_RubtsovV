"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import sys
import psutil
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
)
from PyQt6.QtCore import QThread, pyqtSignal



class CPUMemoryMonitor(QThread):
    # Сигналы для передачи данных в основной поток
    cpu_usage_signal = pyqtSignal(str)
    ram_usage_signal = pyqtSignal(str)

    def __init__(self, delay=1):
        super().__init__()
        self.delay = delay
        self.running = True

    def run(self):
        while self.running:
            # Получаем загрузку CPU и RAM
            cpu_usage = psutil.cpu_percent(interval=None)
            ram_usage = psutil.virtual_memory().percent

            # Отправляем информацию о загрузке
            self.cpu_usage_signal.emit(f"CPU Загрузка: {cpu_usage}%")
            self.ram_usage_signal.emit(f"RAM Загрузка: {ram_usage}%")

            # Задержка для следующего обновления
            self.sleep(self.delay)

    def set_delay(self, delay):
        self.delay = delay


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Монитор загрузки CPU и RAM")
        self.setGeometry(100, 100, 400, 200)
        self.init_ui()
        # Запускаем поток мониторинга
        self.monitor_thread = CPUMemoryMonitor()
        self.monitor_thread.cpu_usage_signal.connect(self.update_cpu_usage)
        self.monitor_thread.ram_usage_signal.connect(self.update_ram_usage)
        self.monitor_thread.start()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        self.delay_input = QLineEdit(self)
        self.delay_input.setPlaceholderText("Введите время задержки (сек.)")
        self.delay_input.setValidator(QtGui.QDoubleValidator(0.1, 60.0, 1, self))
        self.delay_input.textChanged.connect(self.update_delay)
        layout.addWidget(self.delay_input)
        self.cpu_usage_label = QLabel("CPU Загрузка: ")
        layout.addWidget(self.cpu_usage_label)
        self.ram_usage_label = QLabel("RAM Загрузка: ")
        layout.addWidget(self.ram_usage_label)

    def update_delay(self):
        try:
            delay = int(self.delay_input.text())
            self.monitor_thread.set_delay(delay)
        except ValueError:
            pass  # Игнорируем некорректный ввод

    def update_cpu_usage(self, usage_str):
        self.cpu_usage_label.setText(usage_str)

    def update_ram_usage(self, usage_str):
        self.ram_usage_label.setText(usage_str)

    def closeEvent(self, event):
        # Остановка потока при закрытии приложения
        self.monitor_thread.running = False
        self.monitor_thread.quit()
        self.monitor_thread.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())