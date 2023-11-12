import typing
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import(
    QApplication, 
    QWidget, 
    QLineEdit, 
    QPushButton, 
    QFormLayout, 
    QLabel, 
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtCore import QTimer
import json
from dashboard import DashBoard

dashboard = None

def on_enter(window, user, password, loginwindow):

    global dashboard

    # Mở file JSON ở chế độ đọc và ghi
    with open('data.json', 'r+') as f:
        data = json.load(f)

        # Kiểm tra và cập nhật dữ liệu
        if user.text() not in data:
            data[user.text()] = {
                "name": "lamdeptrai",
                "password": password.text(),
                "age": 20,
                "gender": "Male",
                "link": "https://www.facebook.com/mra2322001/"
            }

            # Đưa con trỏ về đầu file và ghi lại dữ liệu mới
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            with open('currentuser.txt', 'w') as current:
                current.write(user.text())
            dashboard = DashBoard(loginwindow)
            QTimer.singleShot(100, window.close)

        


def register(loginwindow):
    window = QWidget()
    layout = QFormLayout()
    user = QLineEdit()
    password = QLineEdit()
    password.setEchoMode(QLineEdit.Password)
    password.returnPressed.connect(lambda: on_enter(window, user, password, loginwindow))
    window.resize(500, 25)
    registerbutton = QPushButton('Register')
    registerbutton.clicked.connect(lambda: on_enter(window, user, password, loginwindow))


    layout = QVBoxLayout()
    user_hbox = QHBoxLayout()
    user_hbox.addStretch(1)
    user_hbox.addWidget(QLabel('Username: '))
    user_hbox.addWidget(user)
    user_hbox.addStretch(1)

    pass_hbox = QHBoxLayout()
    pass_hbox.addStretch(1)
    pass_hbox.addWidget(QLabel('Password: '))
    pass_hbox.addWidget(password)
    pass_hbox.addStretch(1)

    layout.addLayout(user_hbox)
    layout.addLayout(pass_hbox)

    button_hbox = QHBoxLayout()
    button_hbox.addStretch(1)
    button_hbox.addWidget(registerbutton)
    button_hbox.addStretch(1)
    layout.addLayout(button_hbox)

    window.setLayout(layout)

    window.show()