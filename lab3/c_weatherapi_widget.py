"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

import sys
import requests
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QTextBrowser
)
from PyQt6.QtCore import QThread, pyqtSignal
API_KEY = 'baba2e91349e34132c0cf9f53b611283'
class WeatherThread(QThread):
    weather_signal = pyqtSignal(str)
    def __init__(self, latitude, longitude, delay):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.delay = delay
        self.running = True
    def run(self):
        while self.running:
            self.fetch_weather()
            self.sleep(self.delay)
    def fetch_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_info = self.format_weather_info(data)
                self.weather_signal.emit(weather_info)
            else:
                self.weather_signal.emit("Не удалось получить данные о погоде.")
        except Exception as e:
            self.weather_signal.emit(f"Ошибка: {str(e)}")
    @staticmethod
    def format_weather_info(data):
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return (f"Город: {city}, {country}\n"
                f"Температура: {temperature}°C\n"
                f"Погодные условия: {description.capitalize()}")
    def stop(self):
        self.running = False
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Погодное приложение")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()
        self.weather_thread = None
    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        self.latitude_input = QLineEdit(self)
        self.latitude_input.setPlaceholderText("Введите широту (например, 37.7749)")
        layout.addWidget(self.latitude_input)
        self.longitude_input = QLineEdit(self)
        self.longitude_input.setPlaceholderText("Введите долготу (например, -122.4194)")
        layout.addWidget(self.longitude_input)
        self.delay_input = QLineEdit(self)
        self.delay_input.setPlaceholderText("Введите время задержки (сек.)")
        layout.addWidget(self.delay_input)
        self.weather_output = QTextBrowser(self)
        layout.addWidget(self.weather_output)
        self.start_button = QPushButton("Запустить", self)
        self.start_button.clicked.connect(self.start_weather_thread)
        layout.addWidget(self.start_button)
        self.stop_button = QPushButton("Остановить", self)
        self.stop_button.clicked.connect(self.stop_weather_thread)
        layout.addWidget(self.stop_button)
    def start_weather_thread(self):
        try:
            latitude = float(self.latitude_input.text())
            longitude = float(self.longitude_input.text())
            delay = int(self.delay_input.text())
            self.latitude_input.setDisabled(True)
            self.longitude_input.setDisabled(True)
            self.delay_input.setDisabled(True)
            self.start_button.setDisabled(True)
            self.weather_thread = WeatherThread(latitude, longitude, delay)
            self.weather_thread.weather_signal.connect(self.update_weather_info)
            self.weather_thread.start()
        except ValueError:
            self.weather_output.setPlainText("Введите корректные значения широты и долготы.")
    def stop_weather_thread(self):
        if self.weather_thread is not None:
            self.weather_thread.stop()
            self.weather_thread.quit()
            self.weather_thread.wait()
            self.weather_thread = None
            self.latitude_input.setEnabled(True)
            self.longitude_input.setEnabled(True)
            self.delay_input.setEnabled(True)
            self.start_button.setEnabled(True)
    def update_weather_info(self, info):
        self.weather_output.setPlainText(info)
    def closeEvent(self, event):
        self.stop_weather_thread()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())