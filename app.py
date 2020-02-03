from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password= db.Column(db.String(50))





@app.route('/users')
def users():
    user_list = User.query.all()
    users = []


    for user in user_list:
        users.append({'email' : user.email, 'password' : user.password})


    return jsonify({'users' : users})



@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()

    user_creds = user_data['user']

    new_user = User(email=user_creds['email'], password=user_creds['password'])

    db.session.add(new_user)
    db.session.commit()

    return 'Done', 201



@app.route('/login', methods=['POST'])
def login():

    user_data = request.get_json()

    user_creds = user_data['user']

    user_email = User.query.filter_by(email=user_creds['email']).first()

    user_password = User.query.filter_by(password=user_creds['password']).first()

    if not user_email or not user_password:
        return('invalid') 
    else:
        return('valid')





@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"



if __name__ == '__main__':
    app.run(threaded=True, port=5000)

