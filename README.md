# Semantic Docs
A draft for a zero upkeep documentation for [mu-semtech](https://github.com/mu-semtech/).

- Leverages API's to grab all public mu-semtech repos.
- Automatically categorises repos using the mu-semtech naming scheme.
- Manual overrides are possible to hide or move repos between categories.
- Grabs and renders repository README's to generate documentation.
- Easily customisable.
- Requires no client-side JavaScript nor any non-static hosting.
- Can be configured to automatically run on repo changes.

## Usage
```bash
pip3 install -r requirements.txt
python3 app/index.py
```

## Should this be used?

### Pros:
- No Javascript nor server needed! The content will be displayed immediately with no client-side nor server-side rendering required.
- While currently implemented for GitHub, adapting this for a different host should require minimal effort, as as good as all GitHub specific code is separated in a different file.
- Using [Repository Webhooks](https://docs.github.com/en/rest/webhooks) the documentation can automatically be updated whenever changed, not even requiring manual intervention when new repositories are added or current repositories are archived/removed.
- The url changes depending on which documentation you select (although that not being the case in the current docs could also be fixed over time).

### Cons:
- Not a onepager like the current front-end.
- It's less in-tune with mu-semtech (having the docs made in Ember feels fitting due to the large adaptation of Ember in the organisation).
- It currently looks not-very-good to say it lightly, although this can be fixed by implementing the existing styling of the original docs.

## License
The documentation imported belongs to [mu-semtech](https://github.com/mu-semtech/). The code I've written is under the [MIT License](LICENSE).
