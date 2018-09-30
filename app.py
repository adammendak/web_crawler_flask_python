from flask import Flask, send_from_directory, jsonify
from helpers.angular_dist_cleaner import add_static_to_angular_dist_files
from flask_restful import Api
from flask_cors import CORS
from db import db
from resources.domain_with_elements import DomainWithElements
import os

OS_PATH_DIR_NAME = str(os.path.join(os.path.dirname(__file__), "static/index.html"))

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)
CORS(app)  # do developmentu z angulara


#  todo zmienic w single element na enuma
#  todo wczytywac db url ze zmiennch srodowiskowych
#  todo swaggera sprobowac dodac
#  todo dodac postgresa url na razie na sqlite

@app.before_first_request
def create_tables():
    db.create_all()
    add_static_to_angular_dist_files(OS_PATH_DIR_NAME)


@app.route('/',)
def hello_world():
    return send_from_directory('static', 'index.html')


api.add_resource(DomainWithElements, '/domain')

if __name__ == '__main__':
    add_static_to_angular_dist_files(OS_PATH_DIR_NAME)
    app.run()
