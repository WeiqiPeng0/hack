from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import main
from main import Config, generate
import shutil
 
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():

	return render_template('home.html')


@app.route('/generate')
def generate():
    opt = Config()
    main.generate()
    shutil.move("./result.png","static/result.png")

    return render_template('home2.html')

@app.route('/back')
def back():
    return render_template('home.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
