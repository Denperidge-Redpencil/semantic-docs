from os.path import join, realpath, dirname
from os import makedirs
from jinja2 import FileSystemLoader, Environment
from jinja_markdown import MarkdownExtension

def to_docs(types_and_repos):
    """Exports dict(key: str(type), value=[Repo...]) into build/*.html"""
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
            types_and_repos=types_and_repos
        )
        index_file.write(index_content)
    
    # For every type (ember addons, templates...)
    for repo_type in types_and_repos:
        # Get all repos
        repos = types_and_repos[repo_type]

        # Create the output dir (public/Templates)
        repo_type_dir = join(output_dir, repo_type)
        makedirs(repo_type_dir, exist_ok=True)

        # And generate a docpage based on the README for every repo in that type
        for repo in repos:
            readme = repo.get_file("README.md").text

            with open(join(repo_type_dir, repo.name + ".html"), "w") as repo_file:
                repo_content = template_repo.render(types_and_repos=types_and_repos, relative_nav="../", readme=readme)
                repo_file.write(repo_content)



    

