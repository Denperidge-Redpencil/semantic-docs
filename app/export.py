from os.path import join, realpath, dirname
from os import makedirs
from jinja2 import FileSystemLoader, Environment
from jinja_markdown import MarkdownExtension

def to_docs(dict_category_repos):
    """Exports dict(key: str(category), value=[Repo...]) into build/*.html"""
    # Get and create needed dirs
    template_dir = join(realpath(dirname(__file__)), "templates")
    output_dir = realpath(join(dirname(__file__), "..", "build"))

    makedirs(output_dir, exist_ok=True)

    # Setup Jinja environment & templates
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True,
        trim_blocks=True,  # Thanks to https://stackoverflow.com/a/35777386
        lstrip_blocks=True,
        extensions=[
            MarkdownExtension
        ],
    )

    template_index = env.get_template("index.html")
    template_repo = env.get_template("repo.html")

    # Create top-level index.html
    with open(join(output_dir, "index.html"), "w") as index_file:
        index_content = template_index.render(
            dict_category_repos=dict_category_repos
        )
        index_file.write(index_content)
    
    # For every category (ember addons, templates...)
    for category in dict_category_repos:
        # Get all repos
        repos = dict_category_repos[category]

        # Create the output dir (public/Templates)
        category_dir = join(output_dir, category)
        makedirs(category_dir, exist_ok=True)

        print()
        print()
        print(category)
        print("-" * len(category))
        
        # And generate a docpage based on the README for every repo in that category
        for repo in repos:
            readme = repo.get_file("README.md").text

            with open(join(category_dir, repo.name + ".html"), "w") as repo_file:
                repo_content = template_repo.render(dict_category_repos=dict_category_repos, relative_nav="../", readme=readme)
                repo_file.write(repo_content)

            print(repo)




    

