from bottle import Bottle, run, static_file, get, post, request, template
from MySQL.Clientes import Clientes
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
    return template('./HTML/entryPage')
@app.get('/teste')
def teste():
    return template('./HTML/cadastro')

@app.get('/cadastroCli')
def form():
    return template('./HTML/cadastro')

@app.post('/cadastroCli')
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
        return template('./HTML/inserction_success', nome=cli.nome, fone=cli.fone, email=cli.email)
    else:
        return template('./HTML/DBNotFound')
        #return "MySQL não importado." + "nome: " + nome + " fone: " + fone + " email: " + email

run(app, host='localhost', port=8080)