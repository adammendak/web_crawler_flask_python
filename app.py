from flask import Flask, send_from_directory
from helpers.angular_dist_cleaner import add_static_to_angular_dist_files
import os

OS_PATH_DIR_NAME = str(os.path.join(os.path.dirname(__file__), "static/index.html"))

app = Flask(__name__, static_url_path='/static')

add_static_to_angular_dist_files(OS_PATH_DIR_NAME)


#  todo dodac enkoding utf-8
#  todo swaggera sprobowac dodac jak sie da

@app.route('/')
def hello_world():
    return send_from_directory('static', 'index.html')


@app.route('/api/test')
def test():
    return "hello test"


if __name__ == '__main__':
    app.run()
