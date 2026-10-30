# sample-python

A known-good sample for the **Python** starter on [Sparki](https://sparki.tools):
**venv + pip install pytest → pytest on python:3.12**. No requirements.txt and tests at the repo root, so the starter installs only pytest.

## Try it

1. In Sparki, open **Projects → New Project** and add `https://github.com/sparki-tools/sample-python` on branch `main`.
2. On the project, create a pipeline from the **Python** starter.
3. Trigger a build. It should go green.

To see a red build, use branch `fail` instead. It has the same code with one assertion
that cannot hold.

## Why it exists

Third-party repositories change under us: a lockfile is dropped, a Node or Go version moves,
a lint hook is added. This repo is owned by Sparki, has no dependencies, and stays inside
the sandbox's limits: non-root user, read-only root filesystem, writable `/workspace` and
`/tmp`, and a 10-minute step timeout. A first build on it shows the platform working, not
someone else's repo.
