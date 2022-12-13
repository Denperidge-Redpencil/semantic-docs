from re import search, IGNORECASE

"""
Unused, as mu-project is a template but part of core
if repo["is_template"]:
    return repo_types["templates"]
"""
def parse_repo_type(repo):
    if repo["archived"]:
        return repo_types["archive"]
    else:
        for override in overrides:
            if search(override, repo["name"], IGNORECASE):
                return overrides[override]
                
        return _parse_repo_type_from_name(repo["name"])

def _parse_repo_type_from_name(name):
    for repo_type_name in repo_types:
        repo_type = repo_types[repo_type_name]
        if repo_type.check_by_name(name):
            return repo_type
    # Fallback
    return repo_types["tools"]


class RepoType():
    def __init__(self, name, id, regex=""):
        self.name = name
        self.id = id
        self.regex = regex
    
    def check_by_name(self, param):
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

# Sort by override, then specific regex
repo_types = {
    "templates": RepoType("Templates", "templates", r".*-template"),
    "microservices": RepoType("Microservices", "microservices", r".*-service"),
    "ember-addons": RepoType("Ember Addons", "ember-addons", r"ember-.*"),
    "core": RepoType("Core", "core", r"mu-.*"),
    "archive": RepoType("Archive", "archive"),
    "tools": RepoType("Tools", "tools"),
}

overrides = {
    r"mu-cli": repo_types["tools"],
    r"mu-cl-support": repo_types["archive"],
    r"site-.*": repo_types["archive"],
    r"presentation-.*": repo_types["archive"],
}