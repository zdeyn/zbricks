from .hosts.flask import zFlask
from .themes import DefaultTheme

def create_flask(import_name) -> zFlask:
    
    flask = zFlask(import_name)
    flask.attach(DefaultTheme(), 'theme')

    return flask

