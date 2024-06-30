from zbricks import create_flask
from flask import render_template

from zbricks.live.sqla import db

from zbricks.themes import DefaultTheme

def create_app():
    flask = create_flask(__name__)
    flask.attach(DefaultTheme(),'theme')

    @flask.route('/')
    def hello_world():
        return render_template('simple.html', content = 'Hello, World!')

    return flask