from os.path import join, realpath, dirname
from os import makedirs
from jinja2 import FileSystemLoader, Environment

def to_docs(types_and_repos):
    template_dir = join(realpath(dirname(__file__)), "templates")
    output_dir = realpath(join(dirname(__file__), "..", "build"))

    makedirs(output_dir, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True,
        trim_blocks=True,  # Thanks to https://stackoverflow.com/a/35777386
        lstrip_blocks=True,
    )

    template_index = env.get_template("index.html")

    output = template_index.render(
        data=types_and_repos
    )

    with open(join(output_dir, "index.html"), "w") as index:
        index.write(output)


    

