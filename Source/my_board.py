import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QDateTimeEdit, QTableWidget
from PyQt6.QtCore import QDateTime


class EditTaskWindow(QDialog):
    def __init__(self, task_id, title, description):
        super().__init__()
        self.setWindowTitle("Edit Task")
        self.setGeometry(100, 100, 300, 200)
        
        self.task_id = task_id
        
        # Layout
        layout = QVBoxLayout()

        # Title input
        self.title_label = QLabel("Title:")
        layout.addWidget(self.title_label)
        self.title_input = QLineEdit(self)
        self.title_input.setText(title)  # Preencher com o título atual
        layout.addWidget(self.title_input)

        # Description input
        self.desc_label = QLabel("Description:")
        layout.addWidget(self.desc_label)
        self.desc_input = QLineEdit(self)
        self.desc_input.setText(description)  # Preencher com a descrição atual
        layout.addWidget(self.desc_input)

        # Confirm button
        self.edit_button = QPushButton("Edit", self)
        self.edit_button.clicked.connect(self.edit_task_in_db)
        layout.addWidget(self.edit_button)

        self.setLayout(layout)

    def edit_task_in_db(self):
        new_title = self.title_input.text()
        new_description = self.desc_input.text()

        if new_title and new_description:
            # Conectar ao banco de dados e fazer a atualização
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            
            # Atualizar a tarefa no banco de dados
            cursor.execute("""
                UPDATE tasks
                SET title = ?, description = ?
                WHERE id = ?
            """, (new_title, new_description, self.task_id))
            conn.commit()
            conn.close()

            # Fechar a janela de edição
            self.accept()

class AddTaskWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Task")
        self.setGeometry(100, 100, 300, 200)

        # Layout
        layout = QVBoxLayout()

        # Title input
        self.title_label = QLabel("Title:")
        layout.addWidget(self.title_label)
        self.title_input = QLineEdit(self)
        layout.addWidget(self.title_input)

        # Description input
        self.desc_label = QLabel("Description:")
        layout.addWidget(self.desc_label)
        self.desc_input = QLineEdit(self)
        layout.addWidget(self.desc_input)

        # Date input (set with current date and time)
        self.date_label = QLabel("Date:")
        layout.addWidget(self.date_label)
        self.date_input = QDateTimeEdit(self)
        self.date_input.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.date_input)

        # Confirm button
        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.add_task_to_db)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_task_to_db(self):
        title = self.title_input.text()
        description = self.desc_input.text()
        due_date = self.date_input.dateTime().toString("yyyy-MM-dd")

        if title and description:
            # Adiciona ao banco de dados
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()

            # Obter o próximo ID
            cursor.execute("SELECT MAX(id) FROM tasks")
            result = cursor.fetchone()
            next_id = result[0] + 1 if result[0] else 1

            # Inserir nova tarefa
            cursor.execute("INSERT INTO tasks (id, title, description, completed, due_date) VALUES (?, ?, ?, ?, ?)",
                           (next_id, title, description, 0, due_date))
            conn.commit()
            conn.close()

            # Atualizar a tabela
            load_data()

            # Fechar a janela de adição de tarefa
            self.accept()

def init_QTableWidget(window):
    global table
    # Obter a referência ao QTableWidget
    table = window.tableWidget  # Nome definido no Qt Designer

    # Ajustar as colunas para se expandirem conforme o tamanho do QTableWidget
    header = table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    table.setStyleSheet("""
        QTableWidget {
            background-color: #2d2d2d;  /* Cor de fundo do QTableWidget */
            color: rgb(226, 220, 200);              /* Cor do texto */
            gridline-color: #444444;     /* Cor das linhas da grade */
        }
        QHeaderView::section {
            background-color: #3b3b3b;   /* Cor de fundo do cabeçalho */
            color: rgb(226, 220, 200);              /* Cor do texto do cabeçalho */
            padding: 4px;
        }
        QTableCornerButton::section {
            background-color: transparent;   /* Cor de fundo do canto superior esquerdo */
        }
        QTableView {
            selection-background-color: #555555; /* Cor de fundo ao selecionar uma linha */
        }
    """)

    # Carregar os dados do banco de dados
    load_data()

def toggle_task_status(task_id, current_status):
    # Conectar ao banco de dados e alternar o status da tarefa
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    
    new_status = 0 if current_status == 1 else 1
    cursor.execute("""
        UPDATE tasks
        SET completed = ?
        WHERE id = ?
    """, (new_status, task_id))
    conn.commit()
    conn.close()

    # Atualizar a tabela
    load_data()

def load_data():
    global table
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()

    # Executar a consulta
    cursor.execute("SELECT id, title, description, completed FROM tasks")
    rows = cursor.fetchall()

    # Definir o número de linhas e colunas
    table.setRowCount(len(rows))
    table.setColumnCount(4)
    table.setHorizontalHeaderLabels(["ID", "Title", "Description", "Completed"])

    # Ajustar a altura das linhas ao conteúdo
    table.resizeRowsToContents()

    # Preencher a tabela com os dados
    for row_idx, row_data in enumerate(rows):
        for col_idx, data in enumerate(row_data):
            if col_idx == 3:  # Coluna "Completed"
                # Adicionar um botão na coluna "Completed"
                btn = QPushButton("Mark Completed" if data == 0 else "Mark Incompleted")
                btn.clicked.connect(lambda _, row=row_idx, status=data: toggle_task_status(rows[row][0], status))
                table.setCellWidget(row_idx, col_idx, btn)
            else:
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

