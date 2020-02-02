from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password= db.Column(db.String(50))



@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()

    new_user = User(email=user_data['email'], password=user_data['password'])

    db.session.add(new_user)
    db.session.commit()

    return 'Done', 201




@app.route('/users', methods=['GET'])
def respond():
    user_list = User.query.all()
    users = []

    for user in user_list:
        users.append({'email' : user.email, 'password' : user.password})

    return jsonify({'users' : users})




@app.route('/login', methods=['POST'])
def login():

    #admin = User.query.filter_by(id=1).first()

    # user_data = request.get_json()

    # user_creds = user_data['user']

    # if ( (admin.email == user_creds['email']) & (admin.password == user_creds['password']) ):
	#     return('valid')
    # else:
	#     return('invalid')

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user and not check_password_hash(user.password, password):
        return('invalid') 
    else:
        return('valid')





@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"



if __name__ == '__main__':
    app.run(threaded=True, port=5000)

