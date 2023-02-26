PATH = "candidates.json"
from util import load_candidates_from_json, get_candidate
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    s='<ol><br>'
    canditade_list=load_candidates_from_json(PATH)
    for cand in canditade_list:

        s+=f"<li><a href = '/profile/{cand['id']}'>{cand['name']}</li><br>"
    
    s+='</ol>'
    return s

@app.route('/profile/<int:id>')
def profile(id):
    cand = get_candidate(id)
    s=f"<img src={cand['picture']}><br><h1>{cand['name']}</h1><p><b>Позиция: </b>{cand['position']}</p><p><b>Навыки: </b>{cand['skills']}</p>"
    return s

app.run(debug=True)