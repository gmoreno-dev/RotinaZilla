import sys
import os
from datetime import datetime

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QDesktopServices, QIcon
from PyQt6.QtCore import QUrl


app = QtWidgets.QApplication([])
window = uic.loadUi('interface.ui')

# Altera o tema do aplicativo
actual_theme = 0
def alternate_theme(window):
    
    global actual_theme
    if actual_theme == 0:
         actual_theme = 1
         window.setStyleSheet("QMainWindow {background-image: url(./Resources/css2-pattern-by-magicpattern.png)}")
    elif actual_theme == 1:
         actual_theme = 0
         window.setStyleSheet("QMainWindow {background-image: url(./Resources/css-pattern-by-magicpattern.png)}")
     

# Inicialize as variáveis globais
running = 0
task_begin = None
task_end = None
def start_timer(window):
    
    global running
    global task_begin
    global task_end

    icone_inicial = QIcon("./Resources/play-circle.svg")
    icone_final = QIcon("./Resources/pause-circle.svg")

    if running == 0:
        running = 1
        task_begin = datetime.now()
        window.pushButton_5.setIcon(icone_final)
    else:
        running = 0
        task_end = datetime.now()
        window.pushButton_5.setIcon(icone_inicial)
        update_time(task_begin, task_end, window)

def cal_duration(start, end):
    
    if start is not None and end is not None:
        duration = end - start
        return duration.total_seconds() / 3600  # Converte segundos para horas
    else:
        return 0

def update_time(start, end, window):
    
    total_duration = cal_duration(start, end)
    formatted_duration = f"{total_duration:.2f}".replace('.', ',')
    window.label_2.setText(f"{formatted_duration} hours")

#Save notes from the interface (textEdit)
def saveNote(note, window):
    
    # Obtém a data atual e formata como dia-mês-ano
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    # Cria o nome do arquivo com a data
    base_filename = f"notes_{current_date}.txt"

    # Obtém o caminho da área de trabalho do usuário
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Garante que o nome do arquivo seja único
    file_path = os.path.join(desktop_path, base_filename)
    counter = 1
    while os.path.exists(file_path):
        # Cria um novo nome com um número de sufixo
        file_path = os.path.join(desktop_path, f"notes_{current_date}_{counter}.txt")
        counter += 1

    # Salva o conteúdo no arquivo
    with open(file_path, 'w') as archive:
        archive.write(note)
        
    QMessageBox.warning(window, 'Saved notes', f'Notes successfully saved in: {file_path}')

#Open social media buttons
def open_github():

        url = QUrl("https://github.com/gmoreno-dev")
        QDesktopServices.openUrl(url)

def open_linkedin():
        
        url = QUrl("https://www.linkedin.com/in/jgabriel-moreno-dev/")
        QDesktopServices.openUrl(url)
        
def open_instagram():
        
        url = QUrl("https://www.instagram.com/gabmorenogab/")
        QDesktopServices.openUrl(url)

