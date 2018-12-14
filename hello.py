from flask import Flask
app = Flask(__name__)

@app.route('/<label>')
def hello_world(label):
    return 'Hello, %s' % label
