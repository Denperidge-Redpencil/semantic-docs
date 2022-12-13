from re import search, IGNORECASE

def parse_repo_type(repo):
    if repo["archived"]:
        return repo_types["archive"]
    if repo["is_template"]:
        return repo_types["templates"]
    else:
        return _parse_repo_type_from_name(repo["name"])

def _parse_repo_type_from_name(name):
    for repo_type_name in repo_types:
        repo_type = repo_types[repo_type_name]
        if repo_type.check(name):
            return repo_type
    # Fallback
    return repo_types["tools"]


class RepoType():
    def __init__(self, name, id, regex="", overrides=[]):
        self.name = name
        self.id = id
        self.regex = regex
    
    def check(self, param):
        if self.regex:
            return search(self.regex, param, IGNORECASE)
        else:
            return None
    
    def __str__(self) -> str:
        return self.name


"""
The repo class parses the raw GitHub data
to the data that is relevant for docs generation
"""
class Repo():
    def __init__(self, json) -> None:
        self.name = json["name"]
        self.type = parse_repo_type(json)
        self.url = json["html_url"]
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()



repo_types = {
    "templates": RepoType("Templates", "templates", r".*-template"),
    "microservices": RepoType("Microservices", "microservices", r".*-service"),
    "ember-addons": RepoType("Ember Addons", "ember-addons", r"ember-.*"),
    "core": RepoType("Core", "core", r"mu-.*"),
    "tools": RepoType("Tools", "tools"),
    "archive": RepoType("Archive", "archive"),
}
