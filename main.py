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
    cand = get_candidate(id)
    s=f"<img src={cand['picture']}><br><h1>{cand['name']}</h1><p><b>Позиция: </b>{cand['position']}</p><p><b>Навыки: </b>{cand['skills']}</p>"
    return s

app.run(debug=True)