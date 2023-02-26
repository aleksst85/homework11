import json
PATH = "candidates.json"

def load_candidates_from_json(path):
    with open(path, 'r', encoding ='utf-8') as file:
        data = json.load(file)
    return data 



def get_candidate(candidate_id):
    data = load_candidates_from_json(PATH)
    for cand in data:
        if cand["id"] == candidate_id:
            return cand
            break




def get_candidates_by_name(candidate_name):
    data = load_candidates_from_json(PATH)
    for cand in data:
        if cand["name"] == candidate_name:
            return cand
            break

    
def get_candidates_by_skill(skil_name):    
    data = load_candidates_from_json(PATH)
    return_list={}
    for cand in data:
        skils = cand["skills"].split(", ")
        skils =[skil.lower() for skil in skils]
        if skil_name.lower() in skils:
            return_list[cand['id']]=cand
    return return_list

        