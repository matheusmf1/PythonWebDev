from flask import Flask, request, jsonify
from db import db

from Models.produto import Produto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/produto', methods=['POST'])
def produto_post():
  corpo = request.get_json(force=True)
  prod = Produto(**corpo)

  try:
    prod.save()
  except:
    return jsonify({'mensagem':'Ocorreu um erro'}),500

  return jsonify( prod.toDict() ),201

@app.route('/produto/<int:id_entrada>', methods=['GET'])
def produto_get(id_entrada):
  try:
    prod = Produto.select_by_ID(id_entrada)
  except:
    return jsonify({'mensagem': 'Ocorreu um erro interno'}), 500

  if prod:
    return  jsonify( prod.toDict ), 200

  else:
    return jsonify({'mensagem':'Produto não encontrado'}),404

@app.route('/produtos', methods=['GET'])
def produtos_get():
  try:
    prods = Produto.search_all()
  except:
    return jsonify({'mensagem': 'Ocorreu um erro interno'}), 500

  list_dict = []
  for prod in prods:
    list_dict.append(prod.toDict())

  return {'produtos':list_dict},200



@app.before_first_request
def create_Tables():
  db.create_all()

if __name__ == '__main__':
  db.init_app(app)
  app.run(debug=True)