from flask import Flask, request, jsonify
app = Flask(__name__)

admin = {
        "email": "zachziino@pm.me",
        "password": "adminforwx"
    }

@app.route('/users', methods=['GET'])
def respond():

    return jsonify(admin)


@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()

    new_user = User(email=user_data['email'], password=user_data['password'])

    return jsonify(new_user)


@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)