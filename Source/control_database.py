import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('task_manager.db')

# Create a cursor object

cursor = conn.cursor()

# Create a table to store tasks
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 due_date TEXT,
                 completed BOOLEAN DEFAULT 0)''')

def get_completed_tasks():
    cursor.execute("SELECT completed FROM tasks")
    completed_tasks = cursor.fetchall()
    
    return completed_tasks

def get_tasks_from_db():
    # Executar a consulta para buscar todas as tasks
    cursor.execute("SELECT description FROM tasks")
    tasks = cursor.fetchall()
    
    return tasks

def update_task_completion_status(task_description, completed):

    cursor.execute("UPDATE tasks SET completed = ? WHERE description = ?", (completed, task_description))
    
    conn.commit()

get_completed_tasks()

