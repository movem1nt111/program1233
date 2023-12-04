from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

app1 = QApplication([])
w1 = QWidget()
w1.resize(500,500)

l1 = QLabel("Hello, EVERYBODY WELCOME TO LOGIKA!!!")
v1 = QVBoxLayout()
v1.addWidget(l1, alignment = Qt.AlignCenter)

w1.setLayout(v1)
w1.show()
app1.exec_()
