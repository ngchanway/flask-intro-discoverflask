from project import db
from project.models import BlogPost
from project.home.forms import MessageForm
from flask import flash, redirect, url_for, render_template, Blueprint, request
from flask_login import login_required, current_user
# from functools import wraps
from sqlalchemy import exc

# config
home_blueprint = Blueprint(
    'home', __name__, template_folder='templates'
)

# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('users.login'))
#     return wrap

# routes
# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    posts = []
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('home.home'))
    else:
        try:
            posts = db.session.query(BlogPost).all()
        except exc.OperationalError:
            flash('You have no database!')
        return render_template('index.html', posts=posts, form=form, error=error)

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')
