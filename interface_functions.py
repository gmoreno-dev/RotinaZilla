import sys
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

app = QtWidgets.QApplication([])
window = uic.loadUi('interface.ui')

def open_webbrowser():
        print('clicked')
        url = QUrl("https://www.google.com")
        QDesktopServices.openUrl(url)

def clickedButtons():
    window.pushButton_9.clicked.connect(open_webbrowser)