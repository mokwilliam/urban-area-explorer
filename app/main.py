import sys

from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set main window's properties
        self.setWindowTitle("Urban Area Explorer")
        self.setFixedSize(QSize(1280, 720))

        # Set background color
        main_widget = QWidget()
        main_widget.setAutoFillBackground(True)
        palette = main_widget.palette()
        palette.setColor(main_widget.backgroundRole(), QColor("#EEE9E3"))
        main_widget.setPalette(palette)
        main_widget.show()
        self.setCentralWidget(main_widget)

        # Informative status bar
        self.informative_status_bar()

        # Layout
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Select city
        cities_1 = self.city_selector()
        cities_2 = self.city_selector()

        # Add widgets to layout
        layout.addWidget(cities_1)
        layout.addWidget(cities_2)

        # Adjust layout
        layout.setStretchFactor(cities_1, 1)
        layout.setStretchFactor(cities_2, 2)

    def city_selector(self):
        select_city = QComboBox(self)
        cities = [
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Paris",
            "Barcelona",
            "Lisboa",
            "San Diego",
            "Dallas",
            "San Jose",
        ]
        cities.sort()
        select_city.addItems(cities)
        return select_city

    def informative_status_bar(self):
        # Status bar
        self.status_bar_text = QLabel(self)
        self.status_bar = self.statusBar()
        self.status_bar.addPermanentWidget(self.status_bar_text)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._show_time)
        self.timer.start(1000)
        self.remaining_time = 300  # 5 minutes

        self._show_time()

    def _show_time(self):
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.status_bar_text.setText(
            f"Data will be updated in {minutes:02}:{seconds:02}"
        )

        if self.remaining_time == 0:
            self.remaining_time = 300  # Reset timer to 5 minutes
        else:
            self.remaining_time -= 1

        # layout = QVBoxLayout()

        # layout.addWidget(Color("red"))

        # widget = QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
