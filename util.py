import json
PATH = "candidates.json"


def load_candidates_from_json(path):
    with open(path, 'r', encoding ='utf-8') as file:
        _data = json.load(file)
    return _data 


_data=load_candidates_from_json(PATH)

def get_candidate(candidate_id):
    data = load_candidates_from_json(PATH)
    for cand in data:
        if cand["id"] == candidate_id:
            return {'name':cand['name'], "picture":cand["picture"],
                    'position':cand['position'], 'skills':cand['skills']
                    }
    return {'not_found':'Ушел на обед'}




def get_candidates_by_name(candidate_name):
    return [candidate for candidate in _data if candidate_name.lower() in candidate['name'].lower()]


    
def get_candidates_by_skill(skil_name):    
    candidates=[]
    for candidate in _data:
        skills = candidate['skills'].lower().split(', ')
        if skil_name.lower() in skills:
            candidates.append(candidate)
    return candidates
        