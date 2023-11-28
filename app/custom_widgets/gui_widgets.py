from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QComboBox, QWidget


class Color(QWidget):
    def __init__(self, color) -> None:
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
