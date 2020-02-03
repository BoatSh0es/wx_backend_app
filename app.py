from flask import Flask, jsonify, request
#from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'mail.gmx.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'wxsafeflight@gmx.com'
app.config['MAIL_PASSWORD'] = 'wxsafeflight'
app.config['MAIL_DEFAULT_SENDER'] = ('Wx Safe Flight', 'wxsafeflight@gmx.com')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password= db.Column(db.String(50))



# @app.route('/mail')
# def send():
#     msg = Message('Welcome!', recipients=['zachziino@pm.me'])
#     msg.html = '<b>Welcome to Wx Safe Flight! Enjoy, and may good weather be with you!</b>'
#     mail.send(msg)

#     return 'Message has been sent!'


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

    user_creds_register = user_data['user']

    user = User.query.filter_by(email=user_creds_register['email']).first()

    if user: 
        return ('notDone')

    new_user = User(email=user_creds_register['email'], password=user_creds_register['password'])

    db.session.add(new_user)
    db.session.commit()


    return 'Done', 201



@app.route('/login', methods=['POST'])
def login():

    user_data = request.get_json()

    user_creds_login = user_data['user']

    user_email = User.query.filter_by(email=user_creds_login['email']).first()

    user_password = User.query.filter_by(password=user_creds_login['password']).first()

    if not user_email or not user_password:
        return('invalid') 
    else:
        return('valid')




@app.route('/')
def index():
    return "<h1>Welcome to the WX Safe Flight Backend!</h1>"



if __name__ == '__main__':
    app.run(threaded=True, port=5000)

