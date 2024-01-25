from flask import Flask, request

app = Flask(__name__)

seed = [0]

@app.route('/', methods = ["GET"])
def get_request():
    return str(seed[0])

@app.route('/', methods = ["POST"])
def post_request():
    set_seed(seed, request.get_json()["num"])
    return str(seed[0])

def set_seed(seed, num):
    seed[0] = num

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True, port = 8000)