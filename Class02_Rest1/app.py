from flask import Flask, request, jsonify

lista = [ {"id": 0, "nome": "Batata", "preco": 15.45 } ]

app = Flask(__name__)

@app.route( '/produtos', methods = ['GET'] )
def get_produtos():
  resp = { "produtos": lista }
  return jsonify( resp )


@app.route( '/produto/<int:id>', methods = ['POST'] )
def post_produto( id ):
  data = request.get_json()
  item = { "id":id, "nome":data["nome"], "preco":data["preco"] }
  lista.append( item )
  return jsonify( item ),201


@app.route( '/produto/<int:id>', methods = ['PUT'] )
def put_produto( id ):
  data = request.get_json()
  item = { "id": id, "nome": data["nome"], "preco": data["preco"] }

  for i in lista:
    if id in i.values():
      i.update( { "nome":data["nome"], "preco":data["preco"] } )

  return jsonify( item ),201


@app.route( '/produto/<int:id>', methods = ['GET'] )
def get_produto( id ):

  item = {"id": id, "nome": '', "preco": ''}

  for i in lista:
    if id in i.values():
       id = i.get("id")
       nome = i.get("nome")
       preco = i.get("preco")
       item = { "id": id, "nome": nome, "preco": preco }
       return jsonify( item )

  return jsonify({'id':'none'}),404


@app.route( '/produto/<int:id>', methods = ['DELETE'] )
def delete_produto( id ):
  for i in lista:
    if id in i.values():
      lista.remove( i )

  return "Produto deletado",204

if __name__ == '__main__':
  app.run( debug = True )