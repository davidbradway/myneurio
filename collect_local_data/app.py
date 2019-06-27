from flask import Flask, url_for, render_template
from flask_bootstrap import Bootstrap
import datetime
import read_local
import read_remote

data_dir = "data"

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/r/<label>')
def retro(label):
    datastring = read_remote.detect()
    now_str = str(datetime.datetime.now()).replace(":", "_")
    with open('%s/%s_%s.json' % (data_dir, label, now_str), 'w') as f:
        f.write(datastring)
    return 'wrote %s \n %s' % (label, datastring)

@app.route('/<label>')
def write_file(label):
    if 'favicon' in label:
        return 'ignore'
    datastring = read_local.detect()
    now_str = str(datetime.datetime.now()).replace(":", "_")
    with open('%s/%s_%s.json' % (data_dir, label, now_str), 'w') as f:
        f.write(datastring)
    return 'wrote %s \n %s' % (label, datastring)

