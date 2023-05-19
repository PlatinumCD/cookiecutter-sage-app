import re
import sys

NAME_REGEX = r'^[a-z][a-z0-9-]+$'
VERSION_REGEX = r'^[0-9]+\.[0-9]+\.[0-9]+$'

name = '{{ cookiecutter.name }}'
version = '{{ cookiecutter.version }}'

if not re.match(NAME_REGEX, name):
    sys.exit("ERROR: Invalid name! Name must start with a letter and must only consist of lowercase letters, numbers and hyphens.")

if not re.match(VERSION_REGEX, version):
    sys.exit("ERROR: Invalid version! Version must follow x.y.z semvar pattern.")
