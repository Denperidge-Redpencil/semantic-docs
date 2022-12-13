from re import search, IGNORECASE

class RepoType():
    def __init__(self, name, regex=""):
        self.name = name
        self.regex = regex
    
    def check(self, param):
        if self.regex:
            return search(self.regex, param, IGNORECASE)
        else:
            return None
    
    def __str__(self) -> str:
        return self.name

repo_types = {
    "core": RepoType("Core", r""),
    "templates": RepoType("Templates", r""),
    "microservices": RepoType("Microservices", r""),
    "ember-addons": RepoType("Ember Addons", r""),
    "tools": RepoType("Tools"),
    "archive": RepoType("Archive"),
}


def parse_repo_type(repo):
    if repo["archived"]:
        return repo_types["archive"]
    if repo["is_template"]:
        return repo_types["templates"]
    else:
        return _parse_repo_type_from_name(repo["name"])

def _parse_repo_type_from_name(name):
    for repo_type in repo_types:
        print(repo_type)
    
    



"""
The repo class parses the raw GitHub data
to the data that is relevant for docs generation
"""
class Repo():
    def __init__(self, json) -> None:
        print(json)
        self.name = json["name"]
        self.type = parse_repo_type(json)
        self.url = json["html_url"]
    
    def __str__(self) -> str:
        return "{0}: {1}".format(self.type, self.name)
    
    def __repr__(self) -> str:
        return self.__str__()