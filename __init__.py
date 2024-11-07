from flask import Flask, request, redirect, url_for, render_template
from .database import get_db, close_db, init_db

def create_app():
    # Cria uma instância do Flask
    app = Flask(__name__)

    # Rota inicial
    @app.route('/')
    def home():
        return "Bem-vindo ao TaskMaster!"

    # Rota para inicializar o banco de dados (opcional)
    @app.route('/init-db')
    def init_db_route():
        init_db()
        return "Banco de dados inicializado!"

    # Rota para adicionar uma nova tarefa
    @app.route('/add-task', methods=['POST'])
    def add_task():
        title = request.form['title']

        # Verifica se o título não é vazio
        if not title.strip():
            return redirect(url_for('view_tasks', error="O título da tarefa não pode ser vazio."))

        db = get_db()
        db.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
        db.commit()
        return redirect(url_for('view_tasks'))

    # Rota para visualizar todas as tarefas
    @app.route('/tasks')
    def view_tasks():
        db = get_db()
        # Recupera todas as tarefas do banco de dados
        tasks = db.execute('SELECT * FROM tasks').fetchall()

        # Renderiza o template 'tasks.html' e passa as tarefas para ele
        return render_template('tasks.html', tasks=tasks)

    # Rota para marcar a tarefa como concluída
    @app.route('/complete-task/<int:task_id>', methods=['POST'])
    def complete_task(task_id):
        db = get_db()
        db.execute('UPDATE tasks SET completed = ? WHERE id = ?', (True, task_id))
        db.commit()
        return redirect(url_for('view_tasks'))

    # Rota para excluir uma tarefa
    @app.route('/delete-task/<int:task_id>', methods=['POST'])
    def delete_task(task_id):
        db = get_db()
        db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        db.commit()
        return redirect(url_for('view_tasks'))

    # Registra o fechamento do banco de dados ao finalizar o app
    app.teardown_appcontext(close_db)

    return app