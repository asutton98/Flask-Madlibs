from flask import Flask,request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickensRcool"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    prompts = story.prompts
    return render_template('home.html' , prompts = prompts)

@app.route('/story')
def get_story():
    text = story.generate(request.args)
    return render_template('story.html', text = text)