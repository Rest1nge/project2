from PyQt5.QtCore import Qt
from random import randint
from time import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout

def show_winner():
    question.setText('это он!!!')
    button.setText('Ура!')
    a = str(randint(1,1000))
    winner.setText(a)


app = QApplication([])
window = QWidget()

window.resize(600,400)

question = QLabel('Кто победил???')
winner = QLabel('???')
button = QPushButton('узнать ответ')

general_line = QVBoxLayout()

general_line.addWidget(question, alignment = Qt.AlignCenter)
general_line.addWidget(winner, alignment = Qt.AlignCenter)
general_line.addWidget(button, alignment = Qt.AlignCenter)

window.setLayout(general_line)

button.clicked.connect(show_winner)


window.show()
app.exec_()

