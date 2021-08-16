from flask import Flask, request

app = Flask(__name__)

"""
Run like this: 
> flask run --host 0.0.0.0 --port 3000
"""

@app.route('/')
def home():
    return 'hello world!'