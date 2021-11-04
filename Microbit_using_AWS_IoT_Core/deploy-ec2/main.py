from flask import request,Flask
from datetime import datetime as dt
from waitress import serve

app = Flask(__name__)

@app.route("/",methods=['GET'])
def connection_test():
    return {
        'status' : 200,
        'connection' : True
    }

@app.route("/sendData",methods=['GET'])
def send_data():
    datetime = request.args.get('datetime')
    name = request.args.get('name')

    with open('log.txt','a',encoding='utf-8') as file:
        file.write(
            f"{str(dt.now())} [{name}]: Data update at {datetime}."
        )

    return {
        'status' : 200,
        'name' : name,
        'datetime': datetime
    }

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)