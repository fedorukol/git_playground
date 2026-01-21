from flask import Flask 

app = Flask(__name__)

@app.get('/')
def main_page():
    return "Main page mock"

@app.post('/')
def main_page():
    return "Post request mock"
