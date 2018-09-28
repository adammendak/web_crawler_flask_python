from flask import Flask, send_from_directory
from helpers.angular_dist_cleaner import add_static_to_angular_dist_files
from flask_restful import Api
from db import db
import os

OS_PATH_DIR_NAME = str(os.path.join(os.path.dirname(__file__), "static/index.html"))

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

#  todo swaggera sprobowac dodac jak sie da
#  todo dodac postgresa na razie na sqlite zrobic


@app.before_first_request
def create_tables():
    db.create_all()
    add_static_to_angular_dist_files(OS_PATH_DIR_NAME)


@app.route('/')
def hello_world():
    return send_from_directory('static', 'index.html')


@app.route('/api/test')
def test():
    return "hello test"

#  todo tutaj dodac resourcy
# api.add_resource()


if __name__ == '__main__':
    from db import db
    app.run()
