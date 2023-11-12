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

def color(col):
    a = QWidget()
    a.setMinimumSize(200, 200)
    a.setMinimumSize(250, 250)

    a.setStyleSheet(f'background-color: {col}')
    return a

app = QApplication([])

window = QWidget()
layout = QGridLayout()
layout.addWidget(color('black'), 0, 0)
layout.addWidget(color('yellow'), 1, 1)
layout.addWidget(color('yellow'), 1, 2)
window.setLayout(layout)
window.resize(720, 450)

window.show()
app.exec()