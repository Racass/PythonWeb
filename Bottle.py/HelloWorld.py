from bottle import Bottle, run, static_file, get, post, request

import os
import pip #To check if mysql is installed

def checkMySQL():
    try:
        from MySQL.Clientes import Clientes
    except ImportError:
        print("mySQL not installed, so will not work")
        return False
    return True

mySQLImported = checkMySQL() # So I know in runtime if I have MySQL

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
    if(mySQLImported):
        cli = Clientes()
        cli.nome = nome
        cli.fone = fone
        cli.email = email
        cli.Sync()
        return "nome: " + nome + " fone: " + fone + " email: " + email
    else:
        return "MySQL não importado." + "nome: " + nome + " fone: " + fone + " email: " + email

run(app, host='localhost', port=8080)