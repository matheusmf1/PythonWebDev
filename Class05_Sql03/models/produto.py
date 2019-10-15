from db import db

#Implementacao de ORM

class ProdutoModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(80), nullable=False)
  preco = db.Column(db.Float)

  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def toDict(self):
    return {'id': self.id, 'nome': self.nome, 'preco': self.preco}

  @classmethod
  def search_all(cls):
    return cls.query.all()

  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).first()

  def save(self):
    db.session.add( self )
    db.session.commit()

  def delete(self):
    db.session.delete( self )
    db.session.commit()