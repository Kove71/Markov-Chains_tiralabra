import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget
)

from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class ApplicationWidget(QWidget):

    def __init__(self, parent):

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout
        