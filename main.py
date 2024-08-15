from PyQt6 import uic, QtWidgets
from control_database import get_tasks_from_db, update_task_completion_status
from datetime import date
from interface_functions import clickedButtons
import resources

app = QtWidgets.QApplication([])
window = uic.loadUi('interface.ui')

table_values = get_tasks_from_db()

#Alterar o texto da checkBox para os nomes na tabela da database task_manager.db
def tasks_on_main_dashboard(table_values, max_length=11):
    def truncate_text(text, max_length):
        return text if len(text) <= max_length else text[:max_length] + '...'

    # Aplicando a lógica de truncamento diretamente na função
    window.checkBox.setText(truncate_text(str(table_values[0][0]), max_length))
    window.checkBox_2.setText(truncate_text(str(table_values[1][0]), max_length))
    window.checkBox_3.setText(truncate_text(str(table_values[2][0]), max_length))
    window.checkBox_4.setText(truncate_text(str(table_values[3][0]), max_length))
    window.checkBox_5.setText(truncate_text(str(table_values[4][0]), max_length))
    window.checkBox_6.setText(truncate_text(str(table_values[5][0]), max_length))

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
    setup_signals()
    set_date()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()