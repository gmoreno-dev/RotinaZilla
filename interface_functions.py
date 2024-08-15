import sys
import time

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl



app = QtWidgets.QApplication([])
window = uic.loadUi('interface.ui')

def start_timer():
    print('sessss')
    window.label_12.setText("00:00:00")

    start_time = time.time()

    while True:

        elapsed_time = time.time() - start_time

        hours, remainder = divmod(elapsed_time, 3600)

        minutes, seconds = divmod(remainder, 60)

        timer_text = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

        window.label_12.setText(timer_text)

        app.processEvents()  # necessário para atualizar a interface

        time.sleep(0.1)  # atualiza a cada 0.1 segundos

def open_github():

        url = QUrl("https://github.com/gmoreno-dev")
        QDesktopServices.openUrl(url)

def open_linkedin():
        
        url = QUrl("https://www.linkedin.com/in/jgabriel-moreno-dev/")
        QDesktopServices.openUrl(url)
        
def open_instagram():
        
        url = QUrl("https://www.instagram.com/gabmorenogab/")
        QDesktopServices.openUrl(url)

