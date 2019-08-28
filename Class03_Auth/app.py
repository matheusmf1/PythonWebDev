from flask import Flask
from my_auth import basic_auth

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>Navegacao Permitada</h1>'


@app.route('/prot')
@basic_auth
def protecao1():
  return '<h1>Recurso Valioso</h1>'


@app.route('/prot2')
@basic_auth
def protecao2():
  return '<h1>Recurso Valioso 2</h1>'


if __name__ == '__main__':
  app.run( debug = True )