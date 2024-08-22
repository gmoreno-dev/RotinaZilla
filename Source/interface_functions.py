import sys
import os
import sqlite3
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
    inicial_icon = QIcon("./Resources/sun.svg")
    final_icon = QIcon("./Resources/moon.svg")

    global actual_theme

    mDSC1 = '''color: rgb(226, 220, 200);
    border-color: rgb(167, 209, 41);
    border-width: 2px;
    border-radius: 10px;
    border-style: outset;'''
    mDSC2 = '''color: rgb(244, 206, 20);
    border-color: rgb(55, 151, 119);
    border-width: 2px;
    border-radius: 10px;
    border-style: outset;'''
    frame1 = '''color: rgb(226, 220, 200);
    background-color: #3E432E;'''
    frame2 = '''color: rgb(244, 206, 20);
    background-color: #45474B;'''
    progressBar = '''QProgressBar::Chunk{
	background-color: #616F39;
    }
    QProgressBar{
        background-color: rgb(39,39,39);
    }'''
    progressBar2 = '''QProgressBar::Chunk{
	background-color: rgb(55, 151, 119);
    }
    QProgressBar{
        background-color: #45474B;
    }'''
    buttons = '''color: rgb(226, 220, 200);
    border-color: rgb(167, 209, 41);
    border-width: 2px;
    border-radius: 10px;
    border-style: outset;
    background-color: #3E432E;'''
    buttons2 = '''color: rgb(244, 206, 20);
    border-color: rgb(55, 151, 119);
    border-width: 2px;
    border-radius: 10px;
    border-style: outset;
    background-color: #45474B;'''
    circular_buttons = 	'''color: #333;
    border: 2px solid #616F39;
    border-radius: 20px;
    border-style: outset;'''
    circular_buttons2 = '''	color: rgb(244, 206, 20);
    border: 2px solid rgb(55, 151, 119);
    border-radius: 20px;
    border-style: outset;'''
    calendar_widget = '''#calendarWidget QWidget{
	alternate-background-color: #3E432E;
	background-color: rgb(39,39,39);
    }
    '''
    calendar_widget2 = '''#calendarWidget QWidget{
	alternate-background-color: rgb(55, 151, 119);
	background-color: #45474B;
    }
    '''
    checkbox = '''
    QCheckBox::indicator {
        width: 16px;
        height: 16px;
        border-radius: 8px;
        border-style: solid;
        border-width: 2px;
        border-color: #A7D129;

    }
    QCheckBox::indicator:checked {
        width: 16px;
        height: 16px;
        border-radius: 8px;
        border-style: solid;
        border-width: 2px;
        border-color: #A7D129;
        background-color: #616F39;
        
        
        
        image: url(:/Icons/Resources/check.svg);
    }
    QCheckBox{
    border-width: 0px;
    }'''
    checkbox2 = '''
    QCheckBox::indicator {
        width: 16px;
        height: 16px;
        border-radius: 8px;
        border-style: solid;
        border-width: 2px;
        border-color: rgb(55, 151, 119);

    }
    QCheckBox::indicator:checked {
        width: 16px;
        height: 16px;
        border-radius: 8px;
        border-style: solid;
        border-width: 2px;
        border-color: rgb(55, 151, 119);
        background-color: rgb(244, 206, 20);
        
        
        
        image: url(:/Icons/Resources/check.svg);
    }
    QCheckBox{
    border-width: 0px;
    }'''




    if actual_theme == 0:
         window.pushButton_4.setIcon(final_icon)
         actual_theme = 1
         window.setStyleSheet("QMainWindow {background-image: url(./Resources/css2-pattern-by-magicpattern.png)}")
         window.mainDashboardSubContainer.setStyleSheet(mDSC2)
         window.rightDashboardSubContainer.setStyleSheet(mDSC2)
         window.frame.setStyleSheet(mDSC2)
         
         window.frame_3.setStyleSheet('''color: rgb(244, 206, 20);
border-color: rgb(55, 151, 119);
border-width: 2px;
border-radius: 10px;
border-style: outset;''')
         window.frame_4.setStyleSheet(frame2)
         window.frame_5.setStyleSheet(frame2)
         window.frame_6.setStyleSheet(frame2)
         window.frame_7.setStyleSheet(frame2)
         window.frame_8.setStyleSheet(frame2)
         window.frame_9.setStyleSheet(frame2)
         window.frame_10.setStyleSheet(frame2)

         window.progressBar.setStyleSheet(progressBar2)

         window.pushButton.setStyleSheet(buttons2)
         window.pushButton_3.setStyleSheet(buttons2)
         window.pushButton_4.setStyleSheet(buttons2)
         window.pushButton_5.setStyleSheet(circular_buttons2)
         window.pushButton_8.setStyleSheet(circular_buttons2)

         window.calendarWidget.setStyleSheet(calendar_widget2)

         window.checkBox.setStyleSheet(checkbox2)
         window.checkBox_2.setStyleSheet(checkbox2)
         window.checkBox_3.setStyleSheet(checkbox2)
         window.checkBox_4.setStyleSheet(checkbox2)
         window.checkBox_5.setStyleSheet(checkbox2)
         window.checkBox_6.setStyleSheet(checkbox2)
    elif actual_theme == 1:
         window.pushButton_4.setIcon(inicial_icon)
         actual_theme = 0
         window.setStyleSheet("QMainWindow {background-image: url(./Resources/css-pattern-by-magicpattern.png)}")
         window.mainDashboardSubContainer.setStyleSheet(mDSC1)
         window.rightDashboardSubContainer.setStyleSheet(mDSC1)
         window.frame.setStyleSheet(mDSC1)
         
         window.frame_3.setStyleSheet('''color: rgb(226, 220, 200);
         border-color: rgb(167, 209, 41);
         border-width: 2px;
         border-radius: 10px;
         border-style: outset;''')
         window.frame_4.setStyleSheet(frame1)
         window.frame_5.setStyleSheet(frame1)
         window.frame_6.setStyleSheet(frame1)
         window.frame_7.setStyleSheet(frame1)
         window.frame_8.setStyleSheet(frame1)
         window.frame_9.setStyleSheet(frame1)
         window.frame_10.setStyleSheet(frame1)

         window.progressBar.setStyleSheet(progressBar)

         window.pushButton.setStyleSheet(buttons)
         window.pushButton_2.setStyleSheet(buttons)
         window.pushButton_3.setStyleSheet(buttons)
         window.pushButton_4.setStyleSheet(buttons)
         window.pushButton_5.setStyleSheet(circular_buttons)
         window.pushButton_8.setStyleSheet(circular_buttons)

         window.calendarWidget.setStyleSheet(calendar_widget)

         window.checkBox.setStyleSheet(checkbox)
         window.checkBox_2.setStyleSheet(checkbox)
         window.checkBox_3.setStyleSheet(checkbox)
         window.checkBox_4.setStyleSheet(checkbox)
         window.checkBox_5.setStyleSheet(checkbox)
         window.checkBox_6.setStyleSheet(checkbox)

         
     

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

def open_github():

        url = QUrl("https://github.com/gmoreno-dev")
        QDesktopServices.openUrl(url)

def open_linkedin():
        
        url = QUrl("https://www.linkedin.com/in/jgabriel-moreno-dev/")
        QDesktopServices.openUrl(url)
        
def open_instagram():
        
        url = QUrl("https://www.instagram.com/gabmorenogab/")
        QDesktopServices.openUrl(url)

