from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/time')
def time():
    return str(datetime.datetime.now())


if __name__ == '__main__':
    app.run(host='0.0.0.0')