from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment
from builtins import enumerate

app = Flask(__name__)

# Pass enumerate to the Jinja2 environment
app.jinja_env.globals['enumerate'] = enumerate

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'task' in request.form and 'due_date' in request.form:
            task = request.form['task']
            due_date = request.form['due_date']
            tasks.append({'task': task, 'due_date': due_date, 'completed': False, 'reminder_set': False})
        return redirect(url_for('index'))
    return render_template('to_do.html', tasks=tasks)

@app.route('/complete/<int:index>')
def complete_task(index):
    if index < len(tasks):
        tasks[index]['completed'] = not tasks[index]['completed']  # Toggle completion status
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    if index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))

@app.route('/set_reminder/<int:index>', methods=['GET', 'POST'])
def set_reminder(index):
    if index < len(tasks):
        if request.method == 'POST':
            reminder_date = request.form['reminder_date']
            reminder_time = request.form['reminder_time']
            reminder_datetime_str = f"{reminder_date} {reminder_time}"
            tasks[index]['reminder_set'] = True
            tasks[index]['reminder_time'] = reminder_datetime_str
            return redirect(url_for('index'))
        return render_template('set_reminder.html', task_index=index)
    return redirect(url_for('index'))

@app.route('/undo_reminder/<int:index>')
def undo_reminder(index):
    if index < len(tasks):
        tasks[index]['reminder_set'] = False
        tasks[index]['reminder_time'] = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

