import re
import sys

REPO_REGEX = r'^[a-zA-Z][a-zA-Z0-9-]+$'
VERSION_REGEX = r'^[0-9]+\.[0-9]+\.[0-9]+$'

repo = '{{ cookiecutter.repo }}'
version = '{{ cookiecutter.version }}'

if not re.match(REPO_REGEX, repo):
    sys.exit("ERROR: Invalid repo! Repo must start with a letter and must only contain letters, numbers and hyphens.")

if not re.match(VERSION_REGEX, version):
    sys.exit("ERROR: Invalid version! Version must follow x.y.z semvar pattern.")
