import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import QThread, pyqtSignal
from api_key import API_KEY

class WeatherThread(QThread):
    weather_updated = pyqtSignal(str)

    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={API_KEY}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = f"Город: {data['name']}, Температура: {data['main']['temp']}°C, Погода: {data['weather'][0]['description']}"
            self.weather_updated.emit(weather)
        elif response.status_code == 500:
            self.weather_updated.emit("Сайт сломан")
        elif response.status_code == 401:
            self.weather_updated.emit("Некорректный ключ API")
        elif response.status_code == 403:
            self.weather_updated.emit("Нет доступа до сайта")
        else:
            self.weather_updated.emit("Город не найден.")



class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setGeometry(100, 100, 300, 300)
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText('Введите название города')
        self.layout.addWidget(self.city_input)

        self.button = QPushButton('Получить погоду', self)
        self.button.clicked.connect(self.get_weather)
        self.layout.addWidget(self.button)

        self.label = QLabel('Погода будет отображена здесь...')
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.setWindowTitle("Приложение погоды")


    def get_weather(self):
        city = self.city_input.text()
        if city:
            self.thread = WeatherThread(city)
            self.thread.weather_updated.connect(self.update_weather)
            self.thread.start()

    def update_weather(self, weather):
        self.label.setText(weather)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())