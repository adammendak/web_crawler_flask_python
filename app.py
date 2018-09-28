from flask import Flask, send_from_directory
from helpers.angular_dist_cleaner import add_static_to_angular_dist_files
import os

OS_PATH_DIR_NAME = str(os.path.join(os.path.dirname(__file__), "static/index.html"))

app = Flask(__name__, static_url_path='/static')

#  todo dodac enkoding utf-8
#  todo swaggera sprobowac dodac jak sie da
#  todo dodac postgresa na razie na sqlite zrobic


@app.route('/')
def hello_world():
    return send_from_directory('static', 'index.html')


@app.route('/api/test')
def test():
    return "hello test"


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    add_static_to_angular_dist_files(OS_PATH_DIR_NAME)
    app.run()
