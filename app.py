from flask import Flask, request, jsonify
app = Flask(__name__)

admin = {
        "email": "zachziino@pm.me",
        "password": "adminforwx"
    }

admin_email = (list(admin.values())[0])
admin_password = (list(admin.values())[1])


@app.route('/users', methods=['GET'])
def respond():

    return jsonify(admin)


@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()

    user_email = (list(user_data.values())[0])
    user_password = (list(user_data.values())[1])

    return jsonify(user_password)


@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)