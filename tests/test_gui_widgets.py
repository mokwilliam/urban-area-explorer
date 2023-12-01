import pytest
from app.custom_widgets.gui_widgets import BarWidget, Color
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QPainter, QPalette
from PyQt6.QtWidgets import QApplication


@pytest.fixture
def color_widget(request) -> None:
    app = QApplication([])
    color = request.param
    widget = Color(color)
    yield widget
    app.exit()


@pytest.fixture
def bar_widget(request) -> None:
    app = QApplication([])
    color, score = request.param
    widget = BarWidget(QColor(color), score)
    yield widget
    app.exit()


@pytest.mark.parametrize(
    "color_widget",
    ["#ff0000", "#00ff00", "#0000ff"],
    indirect=True,  # allows to parametrize a test with a fixture
)
def test_color_widget(color_widget: Color) -> None:
    assert color_widget.palette().color(QPalette.ColorRole.Window) == QColor(
        color_widget.color
    )


@pytest.mark.parametrize(
    "bar_widget",
    [("#ff0000", 5), ("#00ff00", 8), ("#0000ff", 3)],
    indirect=True,
)
def test_bar_widget(bar_widget: BarWidget) -> None:
    painter = QPainter()
    rect = QRectF(0, 0, 100, 20)
    painter.begin(bar_widget)
    bar_widget.paintEvent(rect)
    painter.end()
