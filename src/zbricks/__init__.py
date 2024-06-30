from .hosts.flask import zFlask

def create_flask(import_name) -> zFlask:
    
    flask = zFlask(import_name)

    return flask

