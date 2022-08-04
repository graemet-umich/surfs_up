from flask import Flask

# create new flask instance
app = Flask(__name__)

#create root starting point
@app.route('/')
def index():
    return 'index'

@app.route('/hello')
def hello_world():
    return 'Hello world'

@app.route('/hard_fib')
def hard_fib():
    return '[0,1,1,2,3,5,8,13]'
