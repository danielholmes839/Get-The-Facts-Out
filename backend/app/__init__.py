# Daniel Holmes
# 2019/9/19
# __init__.py
# sets up the app

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

from app import routes
