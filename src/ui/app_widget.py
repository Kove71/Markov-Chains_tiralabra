import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import (
    QApplication,
    QButtonGroup,
    QLabel,
    QLineEdit,
    QMainWindow,
    QRadioButton,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QWidget,
    QHBoxLayout
)

from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from markov_chain import MarkovChain

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
        self.layout = QHBoxLayout(self)
        self.setup_parameters_ui()
        self.setup_generate_ui()
        self.setup_layout()
    
    def setup_parameters_ui(self):
        """Alustaa parametrikohdan käyttöliittymäelementit.
        """
        self.parameters_layout = QVBoxLayout()
        self.paramater_label = QLabel()
        self.corpus_name_edit = QLineEdit()
        self.corpus_name_edit.setPlaceholderText("Enter the corpus text-file name here")
        self.parameters_layout.addWidget(self.corpus_name_edit)
        self.markov_order_group = QButtonGroup(self)
        self.create_radio_buttons()
        self.parameters_button = QPushButton("Create Markov Model")
        self.parameters_button.clicked.connect(self.paramater_button_clicked)
        self.parameters_layout.addWidget(self.parameters_button)
        self.parameters_layout.addWidget(self.paramater_label)

    def create_radio_buttons(self):
        """Luo vaihtoehdot markov-ketjun asteen valitsemiselle ja 
        liittää ne asetteluun ja nappi-ryhmälle.
        """
        self.buttons = []
        self.rbutton1 = QRadioButton("1st order Markov Chain")
        self.buttons.append(self.rbutton1)
        self.rbutton1.setChecked(True)
        self.rbutton2 = QRadioButton("2nd order Markov Chain")
        self.buttons.append(self.rbutton2)
        self.rbutton3 = QRadioButton("3rd order Markov Chain")
        self.buttons.append(self.rbutton3)
        self.rbutton4 = QRadioButton("4th order Markov Chain")
        self.buttons.append(self.rbutton4)
        self.rbutton5 = QRadioButton("5th order Markov Chain")
        self.buttons.append(self.rbutton5)
        for i, button in enumerate(self.buttons):
            self.parameters_layout.addWidget(button)
            self.markov_order_group.addButton(button, i + 1)

    def setup_generate_ui(self):

        """Alustaa käyttöliittymäkomponentit ja niiden asettelun.
        """

        self.generate_button = QPushButton("Generate!")
        self.generate_button.setEnabled(False)
        self.generate_button.clicked.connect(self.generate_button_clicked)
        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)
        self.generate_layout = QVBoxLayout()

        self.generate_layout.addWidget(self.generate_button)
        self.generate_layout.addWidget(self.text_box)
    
    def setup_layout(self):
        """Asettelee käyttöliittymän elementit
        """
        self.layout.addLayout(self.parameters_layout)
        self.layout.addLayout(self.generate_layout)
        self.setLayout(self.layout)
    
    def paramater_button_clicked(self):
        """Suoritetaan, kun painetaan "Create Markov Model"-nappia.
        Ottaa tekstilaatikon tekstin ja asteen ja antaa ne parametreina
        MarkovChain-luokalle, joka vastaa markov-ketjun luomisesta.
        """
        corpus_name = self.corpus_name_edit.text().strip()
        order = self.markov_order_group.checkedId()
        try:
            self.markov = MarkovChain(order, corpus_name)
            self.generate_button.setEnabled(True)
            self.paramater_label.setText(f"order: {order}\ncorpus: {corpus_name}")
        except Exception as e:
            self.paramater_label.setText(repr(e))


    def generate_button_clicked(self):

        """Suoritetaan, kun painetaan "Generate!"-nappia. 
        Kutsuu generate_sentence-metodia ja tulostaa sen tuottaman
        lauseen käyttöliittymään.
        """
        text = self.markov.generate_text()
        self.text_box.setText(text)
        