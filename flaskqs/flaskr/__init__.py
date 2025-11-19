import os
from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder="../templates",   # <-- THIS FIXES TEMPLATE NOT FOUND
        static_folder="../static"         # <-- Also load static files correctly
    )

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Load the instance config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Simple test route
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # ----- DATABASE SETUP -----
    from . import db
    db.init_app(app)

    # ----- AUTH BLUEPRINT -----
    from . import auth
    app.register_blueprint(auth.bp)

    # ----- BLOG BLUEPRINT -----
    from . import blog
    app.register_blueprint(blog.bp)

    # Default route points to blog.index
    app.add_url_rule('/', endpoint='index')

    return app
