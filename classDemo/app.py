from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route('/test', methods=['POST', 'GET'])
def endPoint1():
    return '<h1>Hello, this is the endPoint test1</h1>'


@app.route('/test2/<int:id>')
def endPoint2(id):
    #no postman /test2/
    return '<h1>Hello, this is the endPoint test2</h1>'


if __name__ == '__main__':
    app.run( debug=True )
