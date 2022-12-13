from requests import get

from Repo import Repo

def list_repos(org="mu-semtech"):
    """ Simply requests all the repos of the specified user/organisation from GitHub API,
    returning the parsed json response
    """
    request = get("https://api.github.com/orgs/{}/repos".format(org))
    return request.json()


def list_and_parse_repos(org="mu-semtech"):
    """ Leverages list_repos, but returns repos parsed into the Repo class
    """
    unparsed_repos = list_repos(org)
    parsed_repos = []
    for repo in unparsed_repos:
        parsed_repos.append(Repo(repo))
    return parsed_repos