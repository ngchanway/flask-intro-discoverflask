from project import db
from project.models import BlogPost
from flask import flash, redirect, session, url_for, render_template, Blueprint
from functools import wraps
from sqlalchemy import exc

# config
home_blueprint = Blueprint(
    'home', __name__, template_folder='templates'
)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

# routes
# use decorators to link the function to a url
@home_blueprint.route('/')
@login_required
def home():
    posts = []
    try:
        posts = db.session.query(BlogPost).all()
    except exc.OperationalError:
        flash('You have no database!')
    return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')
