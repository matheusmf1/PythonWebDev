from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod.db'
db = SQLAlchemy(app)

class Produto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  preco = db.Column(db.Float)

  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def toDict(self):
    return {'id':self.id, 'nome':self.nome, 'preco':self.preco}


@app.route('/produto/', methods=['POST'])
def produto_post():
  corpo = request.get_json(force=True)
  prod = Produto(**corpo)
  #Produto(corpo['nome'], corpo['preco'])

  db.session.add(prod)
  db.session.commit()

  return jsonify( prod.toDict() ), 201


@app.route('/produto/<int:id_entrada>',methods=['GET'])
def produto_get(id_entrada):
  prod = Produto.query.filter_by(id=id_entrada).first()

  if prod:
   return jsonify(prod.toDict())

  return jsonify({'message':'Produto não encontrado'}),404


if __name__ == "__main__":
  db.create_all()
  app.run(debug=True)