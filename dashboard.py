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
from info import Info
from machine_learning.camera import Camera
from machine_learning.voice import Voice

class DashBoard(QWidget):
    cam = None
    voi = None
    def __init__(self, loginwindow, parent: QWidget | None = None, flags: Qt.WindowFlags | Qt.WindowType = Qt.WindowFlags()):
        super().__init__(parent, flags)
        uic.loadUi('dashboard.ui', self)
        self.avatar.clicked.connect(self.info)
        print('showed dashboard')
        self.loginwindow = loginwindow
        self.exit.clicked.connect(self.logout)
        self.show()
        self.voice.clicked.connect(self._voice)
        self.camera.clicked.connect(self._camera)
    
    def _voice(self):
        global voi
        QTimer.singleShot(100, self.close)
        voi = Voice(self)
    def _camera(self):
        global cam
        QTimer.singleShot(100, self.close)
        cam = Camera(self)
    def info(self):
        info = Info(self)
        QTimer.singleShot(100, self.close)
        print('dashboard closed')
    def backagain(self):
        self.show()
    def logout(self):
        QTimer.singleShot(100, self.close)
        self.loginwindow.show()
    
def main():
    app = QApplication([])
    dashboard = DashBoard()
    app.exec()
