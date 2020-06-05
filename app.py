# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash#, g
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
# import sqlite3
import os

# create the application object
app = Flask(__name__)

# app.secret_key = 'my precious'
# # app.database = 'posts.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config.from_object(os.environ['APP_SETTINGS'])
# print(os.environ['APP_SETTINGS'])

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)

# login required decorators
def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return 'Hello, World!' # return a string
    posts = []
    # try:
    #     # g.db = connect_db()
    #     cur = g.db.execute('select * from posts')
    #     posts = [{'title':row[1], 'description':row[2]} for row in cur.fetchall()]
    #     g.db.close()
    # except sqlite3.OperationalError:
    #     flash('You have no database!')
    try:
        posts = db.session.query(BlogPost).all()
    except exc.OperationalError:
        flash('You have no database!')
    return render_template('index.html', posts=posts) # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html') # render a template

# def connect_db():
#     return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
