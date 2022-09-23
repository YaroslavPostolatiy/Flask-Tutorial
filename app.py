from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/app/templates')
def index():
    return render_template('index.html', title='Welcome')

app.run(host='0.0.0.0', port=5002)
