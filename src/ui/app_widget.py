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

    """Käyttöliittymästä vastaava luokka. Perii PyQt5:n QWidget luokan
    ja ui:n pääikkunan.
    """

    def __init__(self, parent):

        """Luokan konstruktori.
        Args:
            parent: pääikkuna, johon luokka "kiinnittyy"
        """

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):

        """Alustaa käyttöliittymäkomponentit ja niiden asettelun.
        """

        self.generate_button = QPushButton("Generate!")
        self.generate_button.clicked.connect(self.generate_button_clicked)
        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)

        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.text_box)
        self.setLayout(self.layout)

    def generate_button_clicked(self):

        """Suoritetaan, kun painetaan "Generate!"-nappia. 
        Kutsuu generate_sentence-metodia ja tulostaa sen tuottaman
        lauseen käyttöliittymään.
        """

        text = generate_sentence(1, "greatgatsby.txt")
        self.text_box.setText(text)
