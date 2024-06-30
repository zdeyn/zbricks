from zbricks import create_flask

def create_app():
    flask = create_flask(__name__)
    
    @flask.route('/')
    def hello_world():
        return 'Hello, World!'

    return flask