from db import db

#Class para manipulacao

class Produto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  preco = db.Column(db.Float)

  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def toDict(self):
    return {'id':self.id, 'nome':self.nome, 'preco':self.preco}

  @classmethod
  def search_all(cls):
    return cls.query.all()

  # Add to dataBase
  def save(self):
    db.session.add(self)
    db.session.commit()

  # Remove from dataBase
  def delete(self):
    db.session.add(self)
    db.session.commit()

  def select_by_ID(self, id):
    return Produto.query.filter_by(id = id).first()
