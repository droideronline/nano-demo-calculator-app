from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    first = data['first']
    second = data['second']
    result = first + second
    return jsonify({'result': result})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    first = data['first']
    second = data['second']
    result = first - second
    return jsonify({'result': result})

if _name_ == '_main_':
    app.run(port=8080, host='0.0.0.0')