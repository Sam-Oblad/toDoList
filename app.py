from flask import Flask, render_template, request

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = request.form.get('task')
        tasks.append({'task' : new_task, 'completed' : False})

        completed_tasks = request.form.getlist('completed')
        for index in completed_tasks:
            tasks[int(index)]['completed'] = True
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run()

