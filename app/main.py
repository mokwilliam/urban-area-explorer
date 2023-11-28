import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import Color
from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Urban Area Explorer")
        self.setFixedSize(QSize(400, 300))

        select_city = QComboBox()
        select_city.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        select_city.addItems(
            [
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
        )

        # Set the central widget of the Window.
        self.setCentralWidget(select_city)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
