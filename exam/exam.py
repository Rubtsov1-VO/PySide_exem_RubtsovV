import sys
import requests
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QTextBrowser,
)

API_KEY = 'baba2e91349e34132c0cf9f53b611283'


class WeatherApp(QMainWindow):
    def __init__(self):
        super(WeatherApp, self).__init__()
        self.setWindowTitle("Приложение погоды")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Введите название города")
        layout.addWidget(self.city_input)
        self.get_weather_button = QPushButton("Получить погоду", self)
        self.get_weather_button.clicked.connect(self.get_weather)
        layout.addWidget(self.get_weather_button)
        self.result_browser = QTextBrowser(self)
        layout.addWidget(self.result_browser)

    def get_weather(self):
        city = self.city_input.text()
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather_info = self.format_weather_info(data)
                self.result_browser.setPlainText(weather_info)
            else:
                self.result_browser.setPlainText("Город не найден.")
        else:
            self.result_browser.setPlainText("Пожалуйста, введите название города.")

    def format_weather_info(self, data):
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']

        weather_info = (f"Город: {city}, {country}\n"
                        f"Температура: {temperature}°C\n"
                        f"Погода: {weather.capitalize()}")
        return weather_info


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())