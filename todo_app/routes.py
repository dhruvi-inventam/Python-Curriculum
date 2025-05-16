from flask import render_template, request, redirect
from app import app, db
from models import Todo

# Home page
@app.route('/')
def index():
    tasks = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)

# Add task
@app.route('/add', methods=['POST'])
def add():
    task_content = request.form['content']
    if task_content.strip():
        new_task = Todo(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect('/')

# Delete task
@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')

# Update task
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', task=task)
