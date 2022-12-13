from re import search, IGNORECASE
from requests import get
import github


def parse_repo_type(json):
    """When given a repo json, determine the repo type"""
    api_parseable = github.parse_repo_type(json)
    if api_parseable != None:
        return repo_types[api_parseable]

    else:
        for override in overrides:
            if search(override, json["name"], IGNORECASE):
                return overrides[override]
                
        return _parse_repo_type_from_name(json["name"])

def _parse_repo_type_from_name(name):
    """When given a name, use regex to determine the repo type"""
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
        """If the type has a regex pattern, check it against the provided parameter"""
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

        # Needed for GitHub's file_url_generator specifically
        self.full_name = json["full_name"]
        self.default_branch =json["default_branch"]
    
    def get_file_url(self, filename):
        return github.file_url_generator(self, filename)
    
    def get_file(self, path):
        """Request a file, appending the repo url if needed"""
        if "http" not in path.lower():
            path = self.get_file_url(path)
        return get(path)
    
    @property
    def readme(self):
        return self.get_file("README.md")
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.__str__()

# Sort by override, then specific regex
# Regex & type names are based on mu-semtech naming conventions
repo_types = {
    "templates": RepoType("Templates", "templates", r".*-template"),
    "microservices": RepoType("Microservices", "microservices", r".*-service"),
    "ember-addons": RepoType("Ember Addons", "ember-addons", r"ember-.*"),
    "core": RepoType("Core", "core", r"mu-.*"),
    "archive": RepoType("Archive", "archive"),  # Not shown on website
    "tools": RepoType("Tools", "tools"),
}

# This for repos not to be included in docs, and/or repos that break the naming conventions
overrides = {
    r"mu-cli": repo_types["tools"],
    r"mu-cl-support": repo_types["archive"],
    r"site-.*": repo_types["archive"],
    r"presentation-.*": repo_types["archive"],
}