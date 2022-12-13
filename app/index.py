from github import list_and_parse_repos
from Repo import repo_types
from export import to_docs

if __name__ == "__main__":
    """Get the repos, parse them, sort them by type, export them to build/*.html"""
    repos = list_and_parse_repos()

    types_and_repos = {}
    for repo_type_id in repo_types:
        repo_type = repo_types[repo_type_id]
        repos_of_type = [repo for repo in repos if repo.type.id == repo_type_id]

        print(repo_type_id)
        print("-----")
        for repo in repos_of_type:
            print(repo)
        print()
        print()

        types_and_repos[repo_type.name] = repos_of_type

    to_docs(types_and_repos)