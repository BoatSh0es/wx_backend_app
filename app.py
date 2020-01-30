from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/users', methods=['GET'])
def respond():
    admin = {
        "email": "zachziino@pm.me",
        "password": "adminforwx"
    }

    return jsonify(admin)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)