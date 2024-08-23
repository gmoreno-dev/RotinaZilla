import time

import sqlite3
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from control_database import get_tasks_from_db, update_task_completion_status, get_completed_tasks
from datetime import date
from interface_functions import open_github, open_linkedin, open_instagram, saveNote, start_timer, alternate_theme
from my_board import init_QTableWidget
from my_board import AddTaskWindow, load_data, EditTaskWindow
import Resources

def update_progress_bar():
    # Conectar ao banco de dados
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    
    # Obter o total de tarefas
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]
    
    if total_tasks == 0:
        # Se não houver tarefas, defina a barra de progresso para 0
        window.progressBar.setValue(0)
        return
    
    # Obter o total de tarefas completadas (onde completed = 1)
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")
    completed_tasks = cursor.fetchone()[0]
    
    # Calcular a porcentagem de tarefas completadas
    completion_percentage = int((completed_tasks / total_tasks) * 100)
    
    # Atualizar a progressBar
    window.progressBar.setValue(completion_percentage)

def update_dashboard():
    # Recarregar os valores da tabela do banco de dados
    table_values = get_tasks_from_db()
    # Atualizar os checkboxes na janela principal
    tasks_on_main_dashboard(table_values)
    # Atualizar o estado das checkboxes (completas ou não)
    completed_tasks = get_completed_tasks()
    update_if_checked()
    # Atualizar os sinais conectados às checkboxes
    setup_signals()
    update_progress_bar()

def remove_all_tasks():
    # Conectar ao banco de dados
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    
    # Remover todas as tarefas do banco de dados
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()

    # Limpar a tabela na interface
    window2.tableWidget.setRowCount(0)

    # Atualizar a tabela (carregar a tabela vazia)
    load_data()
    update_dashboard()
    update_progress_bar()

def remove_task():
    # Obter a linha selecionada da tabela
    selected_row = window2.tableWidget.currentRow()
    
    if selected_row < 0:
        # Nenhuma linha foi selecionada
        return
    
    # Obter o ID da tarefa selecionada (coluna 0 contém o ID)
    task_id = window2.tableWidget.item(selected_row, 0).text()
    
    # Conectar ao banco de dados e remover a tarefa
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    
    # Remover a tarefa pelo ID
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    # Remover a linha da tabela
    window2.tableWidget.removeRow(selected_row)

    # Atualizar a tabela
    load_data()
    update_dashboard()
    update_progress_bar()


def open_edit_task_window():
    # Obter a linha selecionada da tabela
    selected_row = window2.tableWidget.currentRow()
    
    if selected_row < 0:
        # Nenhuma linha foi selecionada
        return
    
    # Obter os valores da tarefa selecionada
    task_id = window2.tableWidget.item(selected_row, 0).text()
    title = window2.tableWidget.item(selected_row, 1).text()
    description = window2.tableWidget.item(selected_row, 2).text()
    
    # Criar uma instância da janela de edição de tarefas, passando os dados da tarefa
    edit_task_window = EditTaskWindow(task_id, title, description)
    
    # Mostrar a janela de edição de tarefas
    if edit_task_window.exec():  # exec() bloqueia até fechar a janela
        # Após a edição, recarregar os dados da tabela
        load_data()
        update_dashboard()
        update_progress_bar()
    

def open_add_task_window():
    # Criar uma instância da janela AddTaskWindow
    add_task_window = AddTaskWindow()
    
    # Mostrar a janela de adição de tarefas
    if add_task_window.exec():  # exec() bloqueia a janela até ser fechada
        # Após fechar a janela, recarregar os dados da tabela
        load_data()
        update_dashboard()
        update_progress_bar()
    
app = QtWidgets.QApplication([])
window = uic.loadUi('interface.ui')
window2 = uic.loadUi('interface2.ui')

table_values = get_tasks_from_db()
completed_tasks = get_completed_tasks()

def init_Window2():
    window2.show()
    init_QTableWidget(window2)

def saveNoteWrapper():
    # Obtém o texto atual do QTextEdit chamado 'textEdit' na janela principal
    notes = window.textEdit.toPlainText()
    
    # Chama a função 'saveNote' passando o texto obtido como argumento
    saveNote(notes, window)

def clickedButtons():

    #Botoes Redes
    window.pushButton_9.clicked.connect(open_github)
    window.pushButton_10.clicked.connect(open_linkedin)
    window.pushButton_11.clicked.connect(open_instagram)

    #Botao Notes
    window.pushButton_8.clicked.connect(saveNoteWrapper)

    #Botoes task time
    window.pushButton_5.clicked.connect(lambda: start_timer(window))

    #Botao setting

    window.pushButton_4.clicked.connect(lambda: alternate_theme(window))

    #Botao my board
    
    window.pushButton_3.clicked.connect(init_Window2)

    #Botoes Tarefas

    window2.pushButton.clicked.connect(open_add_task_window)
    window2.pushButton_2.clicked.connect(open_edit_task_window)
    window2.pushButton_3.clicked.connect(remove_task)
    window2.pushButton_4.clicked.connect(remove_all_tasks)

def tasks_on_main_dashboard(table_values, max_length=11):
    def truncate_text(text, max_length):
        return text if len(text) <= max_length else text[:max_length] + '...'
    
    # Lista de checkboxes
    checkboxes = [
        window.checkBox,
        window.checkBox_2,
        window.checkBox_3,
        window.checkBox_4,
        window.checkBox_5,
        window.checkBox_6
    ]
    
    # Atualizar as checkboxes de acordo com a quantidade de tarefas disponíveis
    for i in range(6):
        if i < len(table_values):  # Se existir uma tarefa no índice `i`
            checkboxes[i].setText(truncate_text(str(table_values[i][0]), max_length))
            checkboxes[i].setVisible(True)  # Mostrar a checkbox
        else:
            checkboxes[i].setText("")  # Limpar o texto da checkbox
            checkboxes[i].setVisible(False)
    update_progress_bar()  # Esconder a checkbox se não houver tarefa

def update_if_checked():
    global completed_tasks

    # Lista de checkboxes
    checkboxes = [
        window.checkBox, 
        window.checkBox_2, 
        window.checkBox_3, 
        window.checkBox_4, 
        window.checkBox_5, 
        window.checkBox_6
    ]

    # Itera sobre a lista de tarefas concluídas e checkboxes
    for i, task in enumerate(completed_tasks):
        if i < len(checkboxes):  # Garante que o índice não ultrapasse a lista de checkboxes
            checkboxes[i].setChecked(task[0] == 1)
    update_progress_bar()

def set_date():
    day = date.today().day
    num = date.today().weekday()
    month = date.today().month
    sem = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    window.label_13.setText(str(day))
    window.label_14.setText(sem[num])
    window.label_15.setText(months[month - 1])
    
#Checar se a tarefa está completa e adicionar ao database
def setup_signals():
    
    window.checkBox.stateChanged.connect(lambda: update_task_completion_status(table_values[0][0], 1 if window.checkBox.isChecked() else 0))
    window.checkBox_2.stateChanged.connect(lambda: update_task_completion_status(table_values[1][0], 1 if window.checkBox_2.isChecked() else 0))
    window.checkBox_3.stateChanged.connect(lambda: update_task_completion_status(table_values[2][0], 1 if window.checkBox_3.isChecked() else 0))
    window.checkBox_4.stateChanged.connect(lambda: update_task_completion_status(table_values[3][0], 1 if window.checkBox_4.isChecked() else 0))
    window.checkBox_5.stateChanged.connect(lambda: update_task_completion_status(table_values[4][0], 1 if window.checkBox_5.isChecked() else 0))
    window.checkBox_6.stateChanged.connect(lambda: update_task_completion_status(table_values[5][0], 1 if window.checkBox_6.isChecked() else 0))

def main():

    clickedButtons()
    tasks_on_main_dashboard(table_values)
    update_if_checked()
    setup_signals()
    set_date()
    update_dashboard()
    update_progress_bar()

    window.show()
    app.exec()
    

if __name__ == '__main__':
    main()