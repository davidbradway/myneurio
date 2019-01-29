from flask import Flask
import datetime
import read_local
app = Flask(__name__)

data_dir = "data"


@app.route('/')
def root():
    return "enter label in URL, e.g.: <a href='http://192.168.1.6:5000/dryer'>192.168.1.6:5000/dryer</a>"


@app.route('/<label>')
def write_file(label):
    if 'favicon' in label:
        return 'ignore'
    datastring = read_local.detect()
    with open('%s/%s_%s.json' % (data_dir, label, datetime.datetime.now()), 'w') as f:
        f.write(datastring)
    return 'wrote %s \n %s' % (label, datastring)
