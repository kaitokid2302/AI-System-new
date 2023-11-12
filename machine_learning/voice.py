import typing
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QFormLayout, 
    QLineEdit, 
    QLabel, 
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QGridLayout
)
class Voice(QWidget):

    def goback(self):
        QTimer.singleShot(100, self.close)
        self.dashboard.show()

    def __init__(self, dashboard, parent: QWidget | None = None, flags: Qt.WindowFlags | Qt.WindowType = Qt.WindowFlags()):
        super().__init__(parent, flags)
        self.resize(1200, 700)
        self.dashboard = dashboard
        self.button = QPushButton('Back', self)
        self.button.setGeometry(70, 20, 113, 32)
        self.button.clicked.connect(lambda: self.goback())
        self.show()
    