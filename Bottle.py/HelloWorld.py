from bottle import Bottle, run, static_file, get, post, request
from MySQL.Clientes import Clientes
import os

app = Bottle()

@app.route('/hello')
def hello():
    return 'Hello World!'
@app.route('/')
def index():
    return '<h3>index</h3>'
@app.get('/teste')
def teste():
    return static_file('cadastro.html', root="./HTML/")
@app.get('/form')
def form():
    return static_file('cadastro.html', root="./HTML/")

@app.post('/form')
def do_form():
    nome = request.forms.get("nome")
    fone = request.forms.get("fone")
    email = request.forms.get("email")
    cli = Clientes()
    cli.nome = nome
    cli.fone = fone
    cli.email = email
    cli.Sync()
    return "nome: " + nome + " fone: " + fone + " email: " + email

run(app, host='localhost', port=8080)