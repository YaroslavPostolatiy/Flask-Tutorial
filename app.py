from flask import Flask

app = Flask(__name__)

app.run(host='0.0.0.0', port=5001)

from flask import render_template

@app.route('/app/templates/index')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

@app.route('/')
@app.route('/app/templates/index')
def index():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('index.html', title='Welcome', members=users)

@app.route('/')
@app.route('/app/templates/exampl', methods = ['POST'])
def exampl():
    name_1 = 'John'
    name_2 = 'Doe'
    return render_template('exampl.html', title='Calculator', number_1=name_1, number_2=name_2)


