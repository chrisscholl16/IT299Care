from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy(app)

USER = "admin"
PASS = "password"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # Retrieve data from the HTML form 'name' attributes
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate credentials
        if username == USER and password == PASS:
            return f"<h1>Welcome, {username}! Login successful.</h1>"
        else:
            error = "Invalid username or password. Please try again."
            
    # Render the login template (passes an error variable if validation failed)
    return render_template('login.html', error=error)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/nurse')
def nurse():
    return render_template('nurse.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)