from control_database import get_tasks_from_db
from PyQt6 import uic, QtWidgets
from datetime import date

app = QtWidgets.QApplication([])
window = uic.loadUi('interface.ui')

