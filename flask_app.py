from flask import Flask,jsonify, request

flask_app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'Name': 'Hunny',
        'Contact': '81********', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Mahin',
        'Contact': '94********', 
        'done': False
    }
]
@flask_app.route("/")
def hello_world():
    return "Hello World!"

@flask_app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)
contact = {
        'id': contacts[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }