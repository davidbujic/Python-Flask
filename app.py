from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/hello/<name>')
def index2(name):
    return render_template('page.html', name = name)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
