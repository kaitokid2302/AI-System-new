from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QFormLayout, 
    QLineEdit, 
    QLabel, 
    QPushButton
)
from PyQt5.QtCore import QTimer
from dashboard import DashBoard
import json
from register import register
app = QApplication([])
window = QWidget()

dashboard = None

def on_enter():
    global dashboard
    f = open('data.json', 'r')
    data = json.load(f)
    print(user.text(), password.text())
    if user.text() in data:
        if(data[user.text()]["password"] == password.text()):
            with open('currentuser.txt', 'w') as current:
                current.write(user.text())
            QTimer.singleShot(100, window.close)
            dashboard = DashBoard(window)
            print('this window is closed')
            
def registerwindow():
    QTimer.singleShot(100, window.close)
    register(window)

layout = QFormLayout()
user = QLineEdit()
password = QLineEdit()
password.setEchoMode(QLineEdit.Password)
password.returnPressed.connect(on_enter)
loginbutton = QPushButton('Login')
loginbutton.clicked.connect(on_enter)
registerbutton = QPushButton('Register')
registerbutton.clicked.connect(registerwindow)

layout.addRow(QLabel('Username'), user)
layout.addRow(QLabel('Password'), password)
layout.addRow(loginbutton, registerbutton)


window.setLayout(layout)
window.resize(500, 200)
window.show()
app.exec_()
