from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from db import db
from helpers.read_database_uri import read_database_uri
from resources.domain_with_elements import DomainWithElements

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = read_database_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)
CORS(app)  # do developmentu z angulara


#  todo zmienic w single element na enuma
#  todo swaggera sprobowac dodac
#  todo dodac postgresa url na razie na sqlite

@app.before_first_request
def create_tables():
    db.create_all()
    read_database_uri()


@app.route('/',)
def hello_world():
    read_database_uri()
    return send_from_directory('static', 'index.html')


api.add_resource(DomainWithElements, '/domain')


if __name__ == '__main__':
    app.run()
