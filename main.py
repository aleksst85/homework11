PATH = "candidates.json"
from util import load_candidates_from_json, get_candidate
from flask import Flask, render_template


app = Flask(__name__)
data=load_candidates_from_json(PATH)

@app.route('/')
def index():
    return render_template('index.html', candidates = data)

@app.route('/profile/<int:id>')
def profile(id):
    candidate = get_candidate(id)
    return render_template('profile.html', candidate = candidate )

app.run(debug=True)