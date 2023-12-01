import pytest
from app.main import MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtTest import QTest


@pytest.fixture
def app(qtbot) -> MainWindow:
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window


def test_city_selection(app: MainWindow, qtbot) -> None:
    main_window = app
    combo_box = main_window.cities

    # Simulate selecting a city
    qtbot.mouseClick(combo_box, Qt.MouseButton.LeftButton)
    QTest.keyClicks(combo_box, "Paris")

    # Check if the selected city matches the expected city
    assert combo_box.currentText() == "Paris"
