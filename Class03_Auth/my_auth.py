from flask import request, make_response
from functools import wraps

def basic_auth(f):

  @wraps( f )
  def process_f( *args, **kwargs ):

    auth = request.authorization
    if auth and auth.username == 'user' and auth.password == 'pass': # desse jeito que se pega as informacoes de auth do cabeçalho
      return f( *args, **kwargs )

    else:
      return make_response('Tentativa sem autenticacao', 401, {'WWW-Authenticate': 'Basic realm=""'})

  return process_f



# decorators funcionam para executar funções dentro de funções, Higher Order Functions