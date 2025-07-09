from flask import Flask, render_template
import importlib
from config import Config


def create_app(modules=[]):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register specified modules
    for module_name in modules:
        module = importlib.import_module(f'modules.{module_name}')
        app.register_blueprint(module.bp)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app


# Example of composing app with selected modules
if __name__ == '__main__':
    # You can configure this list dynamically from env vars or config files
    modules_to_load = ['user_login']
    app = create_app(modules=modules_to_load)
    app.run(debug=True)
