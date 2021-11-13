import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QWidget
)

from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from markov_chain import generate_sentence

class ApplicationWidget(QWidget):

    def __init__(self, parent):

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        self.generate_button = QPushButton("Generate!")
        self.generate_button.clicked.connect(self.generate_button_clicked)
        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)

        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.text_box)
        self.setLayout(self.layout)

    def generate_button_clicked(self):
        text = generate_sentence(1, "greatgatsby.txt")
        self.text_box.setText(text)
