from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'todo.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        conn.execute('''CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )''')
        conn.commit()
        conn.close()

@app.route('/')
def index():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    conn = get_db()
    conn.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    title = request.form['title']
    conn = get_db()
    conn.execute('UPDATE tasks SET title = ? WHERE id = ?', (title, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
