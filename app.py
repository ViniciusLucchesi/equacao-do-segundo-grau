from flask import Flask, render_template, request
from equacao import SegundoGrau


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST',])
def calcular():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    c = int(request.form.get('c'))
    
    equacao = SegundoGrau(a, b, c)
    return render_template('resolution.html', dados=equacao)


if __name__ == '__main__':
    app.run()