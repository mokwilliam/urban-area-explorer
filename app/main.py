import sys

from custom_widgets.gui_widgets import BarWidget
from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
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
        self.setCentralWidget(main_widget)

        # Informative status bar
        self.informative_status_bar()

        # Layout
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Scroll area
        # self.scroll = QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Select city
        self.cities = self.city_selector()

        # Data for the selected city
        # self.data = QWidget()
        # self.dataLayout = QVBoxLayout()

        # Add widgets to layout
        layout.addWidget(self.cities)

        # Dictionary mapping subjects to their colors
        self.subject_colors = {
            "Security": "blue",
            "Transport": "green",
            "Healthcare": "red",
            # Add more subjects with respective colors
        }

        # Dictionary to hold bar widgets for each subject
        self.subject_bars = {}

        # Display bars for different subjects
        for subject in self.subject_colors.keys():
            hbox = QHBoxLayout()
            label = QLabel(subject)
            hbox.addWidget(label)
            bar_widget = BarWidget(self.subject_colors[subject], 1)
            self.subject_bars[subject] = bar_widget
            hbox.addWidget(bar_widget)
            layout.addLayout(hbox)

        # Adjust layout
        # layout.setStretchFactor(cities, 1)
        # layout.setStretchFactor(cities_2, 2)

    def city_selector(self):
        select_city = QComboBox(self)
        cities = [
            "New York",
            "Los Angeles",
            "Chicago",
            "Houston",
            "Paris",
        ]
        cities.sort()
        select_city.addItems(cities)
        select_city.currentIndexChanged.connect(self.update_dashboard)
        select_city.setCurrentIndex(0)
        return select_city

    def update_dashboard(self):
        current_city_index = self.cities.currentIndex()
        # Simulated data update for different subjects
        # You can replace this with actual data retrieval logic for the selected city
        city_data = {
            "New York": {"Security": 8, "Transport": 1, "Healthcare": 7},
            "Los Angeles": {"Security": 6, "Transport": 9, "Healthcare": 1},
            "Chicago": {"Security": 1, "Transport": 7, "Healthcare": 6},
            "Houston": {"Security": 4, "Transport": 5, "Healthcare": 2},
            "Paris": {"Security": 7, "Transport": 10, "Healthcare": 4},
        }
        selected_city = self.cities.itemText(current_city_index)
        city_scores = city_data.get(selected_city, {})

        # Update bars based on the selected city's scores
        for subject, score in city_scores.items():
            bar_widget = self.subject_bars.get(subject)
            if bar_widget:
                bar_widget.score = score
                bar_widget.update()

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


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
