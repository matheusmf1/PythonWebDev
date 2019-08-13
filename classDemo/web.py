from flask import Flask, jsonify, request

app = Flask( __name__ )

@app.route('/') #root
def home():
    return "Can i return any html here?"

@app.route('/services') #services
def serv():
    dict = { 'services': ['Walk with the dog', 'Teach', 'Write'] }
    return jsonify( dict )

@app.route('/add', methods=['POST']) #My Method
def add():
    req = request.get_json()
    result = req['a'] + req['b']
    return jsonify( {'Result':result} )


if __name__ == '__main__':
    app.run(debug=True)