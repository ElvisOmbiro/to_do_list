from flask import Flask, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password)
    # Save the username and hashed_password to the database
    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Retrieve the user's hashed password from the database
    if check_password_hash(hashed_password, password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    return 'Login Failed'

