from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QColor, QPainter, QPainterPath, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color) -> None:
        super().__init__()
        self.setAutoFillBackground(True)

        self.color = color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class BarWidget(QWidget):
    def __init__(self, color, score):
        super().__init__()
        self.color = QColor(color)
        self.score = score

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), Qt.GlobalColor.lightGray)

        filled_width = self.width() - (self.width() * (self.score / 10))
        filled_rect = self.rect().adjusted(0, 0, -round(filled_width), 0)

        path = QPainterPath()
        path.addRoundedRect(QRectF(filled_rect), 5, 5)
        painter.fillPath(path, self.color)
