# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash#, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
# import sqlite3

# create the application object
app = Flask(__name__)

app.secret_key = 'my precious'
# app.database = 'posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *

# login required decorators
def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
            flash('You need to login first.')
            return redirect('login')
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return 'Hello, World!' # return a string
    # posts = []
    # try:
    #     # g.db = connect_db()
    #     cur = g.db.execute('select * from posts')
    #     posts = [{'title':row[1], 'description':row[2]} for row in cur.fetchall()]
    #     g.db.close()
    # except sqlite3.OperationalError:
    #     flash('You have no database!')
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts) # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html') # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

# def connect_db():
#     return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
