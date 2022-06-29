from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    logging.info('we are testing logging module')
    return 'Starting ML project   CI CD Pipeline has been established'


if __name__ == '__main__':
    app.run(debug=True)