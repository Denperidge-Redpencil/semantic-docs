from re import search, IGNORECASE

repo_types = {
    "core": {
        "name": "Core",
        "regex": r"",
    },
    "template": {
        "name": "Templates",
        "regex": r"",
    },
    "microservices": {
        "name": "Microservices",
        "regex": r"",
    },
    "ember": {
        "name": "Ember Addons",
        "regex": r"",
    },
    "tools": {
        "name": "Tools"
    },
    "archive": {
        "name": "Archive"
    }
}


def parse_repo_type(repo):
    if repo["archived"]:
        return repo_types.archive.name
    if repo["is_template"]:
        return repo_types.template.name
    else:
        return _parse_repo_type_from_name(repo["name"])

def _parse_repo_type_from_name(name):
    for repo_type in repo_types:
        print(repo_type)
    if search(repo_types.template.regex, IGNORECASE):
        return repo_types.template.name
    



"""
The repo class parses the raw GitHub data
to the data that is relevant for docs generation
"""
class Repo():
    def __init__(self, json):
        print(json)
        self.name = json["name"]
        self.type = parse_repo_type(json)
        self.url = json.html_url