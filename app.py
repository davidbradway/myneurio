from flask import Flask
import datetime
import read_local
app = Flask(__name__)

@app.route('/<label>')
def write_file(label):
    datastring = read_local.detect()
    with open('%s_%s.json' % (label, datetime.datetime.now()), 'w') as f:
        f.write(datastring)
    return 'wrote %s \n %s' % (label, datastring)
