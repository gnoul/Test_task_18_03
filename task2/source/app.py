from random import random
from time import sleep
from os import environ as env

from flask import Flask


DIR = 'source_files'
FILENAME = env.get('filename', 'source1')
ERROR_RATE = 0.75
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if random() > ERROR_RATE:
        sleep(5)
    with open(f'{DIR}/{FILENAME}', 'r') as f:
        res = f.read()
    response = app.response_class(
        response=res,
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
