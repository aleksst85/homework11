PATH = "candidates.json"
from util import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
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


@app.route('/search/<name>')
def search(name):
    candidate_name = get_candidates_by_name(name)
    return render_template('search.html', candidates = candidate_name, candidates_len=len(candidate_name) )


@app.route('/skills/<skill>')
def search_skills(skill):
    candidate_skills = get_candidates_by_skill(skill)
    return render_template('skills.html', candidates = candidate_skills, candidate_len = len(candidate_skills), skill=skill) 




app.run()