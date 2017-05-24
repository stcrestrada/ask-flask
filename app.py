from flask import Flask, session
from flask_cors import CORS

from config import DEBUG, HOST, PORT, SECRET_KEY

from resources.instances import instances_api
from resources.authenticate import authenticate_api

import models

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.register_blueprint(instances_api, url_prefix="/api/v1")
app.register_blueprint(authenticate_api, url_prefix="/api/v1")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return "Hello World."

if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)
