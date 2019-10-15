from flask_restful import Resource
from flask import request

from models.produto import ProdutoModel

#Implementacao das 4 rotas

# Não precisa mais do jsonify, esse cara já está fazendo isso

class Produto(Resource):

  def get( self, id_entrada = None ):

    if id_entrada:
      try:
        prod = ProdutoModel.find_by_id(id_entrada)

      except:
        return {'mensagem': 'Ocorreu um erro interno'}, 500

      if prod:
        return prod.toDict(), 200

      else:
        return {'mensagem': 'Produto não encontrado'}, 404

    else:
      #Show them all
      try:
        todos = ProdutoModel.search_all()
      except:
        return {'mensagem': 'Ocorreu um erro interno'}, 500

      lista_prod = []
      for prod in todos:
        lista_prod.append(prod.toDict())

      return {'produtos': lista_prod}, 200


  def post( self,id_entrada = None ):
    corpo = request.get_json(force=True)
    prod = ProdutoModel(**corpo)  # Produto(corpo['nome'], corpo['preco'])
    try:
      prod.save()
    except:
      return {'mensagem': 'Ocorreu um erro interno'}, 500

    return prod.toDict(), 201


  def put( self,id_entrada = None ):
    pass


  def delete(self,id_entrada = None ):

    if id_entrada:
      try:
        prod = ProdutoModel.find_by_id(id_entrada)

      except:
        return {'mensagem': 'Ocorreu um erro interno'}, 500

      try:
        if prod:
          prod.delete()
          return {'mensagem': 'Item deletado'}, 200

      except:
        return {'mensagem': 'Ocorreu um erro interno'}, 500

      return {'mensagem': 'Produto não encontrado'}, 404

    else:
      return {'mensagem': 'Informe um id'}, 403 #OU 400
