from flask import Flask, request, jsonify
from flask_restful import Api
from db import db

from resources.produto import Produto


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource( Produto, '/produto/<int:id_entrada>', '/produto' )

@app.before_first_request
def create_tables():
  db.create_all()

if __name__ == "__main__":
  db.init_app(app)
  app.run(debug=True)