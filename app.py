from flask import Flask, request, jsonify
import urllib.parse
app = Flask(__name__)

admin = {
        "email": "admin@admin.com",
        "password": "admin"
    }

admin_email = (list(admin.values())[0])
admin_password = (list(admin.values())[1])

valid_login = 'valid'

invalid_login = 'invalid'


@app.route('/users', methods=['GET'])
def respond():

    return jsonify(admin)


@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()

    user_creds = user_data['user']

    user_email = user_creds['email']

    user_password = user_creds['password']

    if ( (admin_email == user_email) & (admin_password == user_password)  ):
	    return(valid_login)
    else:
	    return(invalid_login)



@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)