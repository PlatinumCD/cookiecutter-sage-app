# Cookiecutter Template for Sage Apps

This repo is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to quickly bootstrap new Sage apps.

## Usage

First, make sure you've installed cookiecutter:

```sh
pip3 install --upgrade cookiecutter
```

Then, run the following:

```sh
cookiecutter gh:waggle-sensor/cookiecutter-sage-app
```

You'll be prompted for a few things like:

```txt
  [1/5] name (my-amazing-app-name): my-amazing-app-name
  [2/5] description (My really amazing app!):
  [3/5] author (My name):
  [4/5] version (0.1.0):
  [5/5] Select kind
    1 - vision
    2 - usbserial_sensor
    3 - minimal
    4 - tutorial
    Choose from [1/2/3/4] (1): 1
```

After that, you'll have a new app in the directory you provided for `name` with the following files:

| Name | Description |
|------|-------------|
| main.py | Main code |
| requirements.txt | Code dependencies |
| Dockerfile | App build instructions |
| sage.yaml | App metadata |
