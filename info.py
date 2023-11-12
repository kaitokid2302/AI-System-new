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
    QGridLayout,
    QCheckBox
)
import json

class Info(QWidget):

    def _currentuser(self):
        self.currentuser = ""
        with open('currentuser.txt', 'r') as current:
            self.currentuser = current.read()
            self.currentuser.strip()

    def save_info(self):
        with open('data.json', 'r+') as f:
            data = json.load(f)
            data[self.currentuser]["name"] = self.name.text()
            data[self.currentuser]["age"] = int(self.age.text())
            data[self.currentuser]["link"] = self.link.text()
            if self.male.isChecked():
                data[self.currentuser]["gender"] = "Male"
            else:
                data[self.currentuser]["gender"] = "Female"

            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        self.backtodashboard()

    def backtodashboard(self):
        QTimer.singleShot(100, self.close)
        self.dashboard.backagain()
    def __init__(self, dashboard, parent: QWidget | None = None, flags: Qt.WindowFlags | Qt.WindowType = Qt.WindowFlags()):
        super().__init__(parent, flags)
        self._currentuser()
        uic.loadUi('infor.ui', self)
        self.save.clicked.connect(lambda: self.save_info())
        self.dashboard = dashboard
        data = json.load(open('data.json', 'r'))
        self.name.setText(data[self.currentuser]["name"])
        self.age.setText(str(data[self.currentuser]["age"]))
        self.link.setText(data[self.currentuser]["link"])
        user_gender = data[self.currentuser].get("gender", "Male")
        if user_gender == "Male":
            self.male.setChecked(True)
            self.female.setChecked(False)
        elif user_gender == "Female":
            self.female.setChecked(True)
            self.male.setChecked(False)
        self.back.clicked.connect(self.backtodashboard)
        self.show()