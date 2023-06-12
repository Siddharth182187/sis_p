from flask import *
import json, time

app = Flask(__name__)
@app.route('/login', methods=['GET'])
def login():
    data_set = {
                "evt": "LS",
                "gtp": "password",
                "lid": "jyainfottech@gmail.com",
                "pwd": "JYA@123",
                "scp": "api",
                "tid": "12389"
                }
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/d2c', methods=['GET'])
def d2c():
    user_query= str(request.args.get('user')) # /user/?user=USER_NAME
    data_set = {'Page': 'Request', 'Message': 'Successfully got the request for' + (user_query), 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/v2/ntfy', methods=['GET'])
def ntfy():
    data_set = {'Page': 'Home', 'Message': 'Successfully loaded the Home page', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(debug=True)
