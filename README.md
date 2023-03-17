# Cookiecutter Template for Sage Apps

This repo is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to quickly bootstrap new Sage apps.

## Usage

First, make sure you've installed cookiecutter:

```sh
pip3 install cookiecutter
```

Then, run the following:

```sh
cookiecutter gh:waggle-sensor/cookiecutter-sage-app
```

You'll be prompted for a few things like:

```txt
name [My Amazing App]: 
repo [my_amazing_app]: 
description [My really amazing app!]: 
author [My name]: 
version [0.1.0]: 
Select template:
1 - vision
2 - usbserial_sensor
3 - minimal
Choose from 1, 2, 3 [1]: 
```

After that, you'll have a new app directory named with the repo name you provided.
