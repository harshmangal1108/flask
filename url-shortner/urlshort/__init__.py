from flask import Flask

def create_app(test_config=None): 
    app = Flask(__name__)
    # This allows us to securly send messgaes back and forth to the user so that they can't see this info
    app.secret_key='hajaljhaksxakusyxajxuaydcxka'

    from . import urlshort
    app.register_blueprint(urlshort.bp)
    return app