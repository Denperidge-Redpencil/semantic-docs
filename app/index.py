from data_fetch import list_and_parse_repos
from Repo import repo_types

if __name__ == "__main__":
    repos = list_and_parse_repos()
    print(len(repos))
    
    for repo_type_name in repo_types:
        print(repo_type_name)
        print("-----")
        repos_of_type = [repo for repo in repos if repo.type.id == repo_type_name]
        for repo in repos_of_type:
            print(repo)
        print()
        print()