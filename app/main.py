from app.custom_widgets.gui_widgets import BarWidget
from app.database.data import get_data, simulate_update_data
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

SUBJECTS_COLORS = {
    "Housing": "#f3c32c",
    "Cost of Living": "#f3d630",
    "Startups": "#f4eb33",
    "Venture Capital": "#d2ed31",
    "Travel Connectivity": "#7adc29",
    "Commute": "#36cc24",
    "Business Freedom": "#19ad51",
    "Safety": "#0d6999",
    "Healthcare": "#051fa5",
    "Education": "#150e78",
    "Environmental Quality": "#3d14a4",
    "Economy": "#5c14a1",
    "Taxation": "#88149f",
    "Internet Access": "#b9117d",
    "Leisure & Culture": "#d10d54",
    "Tolerance": "#e70c26",
    "Outdoors": "#f1351b",
}


class MainWindow(QMainWindow):
    """Main window of the application"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize the UI"""
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

        # Data
        self.data = get_data()
        self.data_cities = self.data["urban_areas"]

        # Select city
        self.cities = self.city_selector()

        # Add widgets to layout
        layout.addWidget(self.cities)

        # Dictionary to hold bar widgets for each subject
        self.subject_scores = {}
        self.subject_bars = {}

        # Display bars for different subjects
        for subject in SUBJECTS_COLORS.keys():
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(subject))
            score = next(iter(self.data_cities.values()))[subject]
            text_score = QLabel(str(round(score, 2)))
            hbox.addWidget(text_score)
            bar_widget = BarWidget(SUBJECTS_COLORS[subject], score)
            self.subject_scores[subject] = text_score
            self.subject_bars[subject] = bar_widget
            hbox.addWidget(bar_widget)
            layout.addLayout(hbox)

        # Adjust layout
        # layout.setStretchFactor(cities, 1)
        # layout.setStretchFactor(cities_2, 2)

    def city_selector(self) -> QComboBox:
        """Create a combo box to select a city

        Returns:
            QComboBox: Combo box to select a city
        """
        select_city = QComboBox(self)
        cities: list = list(self.data_cities.keys())
        cities.sort()
        select_city.addItems(cities)
        select_city.currentIndexChanged.connect(self.update_dashboard)
        select_city.setCurrentIndex(0)
        return select_city

    def update_dashboard(self) -> None:
        """Update dashboard based on the selected city"""
        current_city_index = self.cities.currentIndex()

        selected_city = self.cities.itemText(current_city_index)
        city_scores = self.data_cities.get(selected_city, {})

        # Update bars based on the selected city's scores
        for subject, score in city_scores.items():
            text_score = self.subject_scores.get(subject)
            bar_widget = self.subject_bars.get(subject)
            if bar_widget:
                text_score.setText(str(round(score, 2)))
                bar_widget.score = score
                bar_widget.update()

    def informative_status_bar(self) -> None:
        """Create an informative status bar"""
        # Status bar
        self.status_bar_text = QLabel(self)
        self.status_bar = self.statusBar()
        self.status_bar.addPermanentWidget(self.status_bar_text)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._show_time)
        self.timer.start(1000)
        self.remaining_time = 10  # 10 seconds

        self._show_time()

    def _show_time(self) -> None:
        """Show remaining time in the status bar"""
        minutes: int = self.remaining_time // 60
        seconds: int = self.remaining_time % 60
        self.status_bar_text.setText(
            f"Data will be updated in {minutes:02}:{seconds:02}"
        )

        if self.remaining_time == 0:
            self.remaining_time = 10  # Reset timer to 10 seconds
            self.data_cities = simulate_update_data()["urban_areas"]
            self.update_dashboard()
        else:
            self.remaining_time -= 1


def main():
    """Main function"""
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
