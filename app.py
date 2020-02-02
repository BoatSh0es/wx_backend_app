from flask import Flask, jsonify, request
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

    return jsonify(user_list)




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

