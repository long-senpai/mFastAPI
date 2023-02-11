from flask import Flask, request, Blueprint

from blueprints.basic_endpoints import blueprint as basic_endpoints

app = Flask(__name__)
app.register_blueprint(basic_endpoints)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8000)
