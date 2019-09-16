from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Set the path of SQLite uri
dataBaseDir = os.path.abspath(os.path.dirname(__file__))
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///mydb.sqlite'

#after creating the Model we have to create the dataBase, for this open python console,
#from app import db
# db.create_all()

# Here we're binding the db and ma with the app
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Here is the User db model
class User( db.Model ):
  id = db.Column( db.Integer, primary_key = True )
  userName = db.Column( db.String(80), unique = True )
  email = db.Column( db.String(120), unique = True )

  def __init__(self, username, email):
    self.userName = username
    self.email = email



# Here it's defined how JSON's response struct will be like
class UserSchema( ma.Schema ):
  class Meta:
    #Fields to expose
    fields = ('id','userName', 'email')


user_schema = UserSchema()
users_schema = UserSchema( many = True ) # instance of list of UserSchema



@app.route("/user", methods = ["POST"])
def add_user():
  userName = request.json['userName']
  email = request.json['email']

  new_user = User( userName, email )

  if db.session.query(User).filter_by( email = email ).count() > 0:
    return jsonify('This user exist')

  else:
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify( new_user )



@app.route("/user", methods = ["GET"])
def get_user():
  all_users = User.query.all()
  result = users_schema.dump(all_users)

  return jsonify( result )


@app.route("/user/<id>", methods = ["GET"])
def user_detail( id ):
  user = User.query.get(id)
  return user_schema.jsonify(user)


@app.route("/user/<id>", methods = ["PUT"])
def user_update( id ):
  user = User.query.get(id)
  userName = request.json['userName']
  email = request.json['email']

  user.email = email
  user.userName = userName

  db.session.commit()
  return user_schema.jsonify( user )


@app.route("/user/<id>", methods = ["DELETE"])
def user_delete( id ):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify( user )

if __name__ == '__main__':
  app.run( debug = True )