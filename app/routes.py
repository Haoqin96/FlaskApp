from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def hello_world():  # put application's code here
    user = {'username': 'hwu'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC346', 'title': 'Enterprise System with Java'}, 'instructor': 'Evan Noynaert'},
               {'classInfo': {'code': 'CSC374', 'title': 'UNIX/Linux System Administration'},
                'instructor': 'Baoqiang Yan'},
               {'classInfo': {'code': 'CSC305', 'title': 'Database Architecture and Concepts'},
                'instructor': 'Baoqiang Yan'}, ]
    return render_template('index.html', title='Home', user=user, classes=classes)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
