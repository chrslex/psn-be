from flask import Flask, g
from repository.db.conn import get_db_connection

def close_db_connection(exception=None):
    db_connection = g.pop('db_connection', None)
    if db_connection is not None:
        db_connection.close()

def create_app():
    app = Flask(__name__)

    @app.before_request
    def before_request():
        g.db_connection = get_db_connection()

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        db = getattr(g, 'db_connection', None)
        if db is not None:
            db.close()

    # register routes
    from repository.customer import customer_bp
    app.register_blueprint(customer_bp, url_prefix='/customer')

    return app
