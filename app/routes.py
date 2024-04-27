from app import app
from .models import User 
from markupsafe import escape 
from flask import render_template, redirect, url_for, \
request, flash 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome {escape(name)}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check user database 
        user = User(username, password) 
        exists, authenticated = user.signIn() 

        # authenticated = (username == 'kilian' and password == '1234')
        if exists: 
            if authenticated:
                return redirect(url_for('success', name=username))
            else:
                flash('password did not match username')
                return render_template('login.html')
        else: 
            flash('User does not exist')
            return render_template('login.html')
    else:
        return render_template('login.html')
    
