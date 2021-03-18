from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Leonardo'}
    posts = [
        {'author': {'username':'Maria'}, 'body': "Ola da Maria"},
        {'author': {'username':'Feulo'}, 'body': "Ola"}
    ]
    return render_template("index.html", user=user, posts=posts)