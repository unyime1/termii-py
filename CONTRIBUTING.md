# Contributing to Termii-py

We'd love you to contribute to Termii-py!


## Issues

Questions, feature requests and bug reports are all welcome as discussions or issues. However, to report a security vulnerability, please send an email to `lordunyime@gmail.com`.


## Prerequisites

You'll need the following prerequisites:

1. Any Python version between Python 3.8 and 3.12
2. virtualenv or other virtual environment tool
3. git
4. make


## Installation and setup

Fork the repository on GitHub and clone your fork locally.

```bash
# Clone your fork and cd into the repo directory
git clone git@github.com:<your username>/termii-py.git
cd termii-py

# Setup virtualenv
python3.10 -m venv venv
source venv/bin/activate

# Install developement packages.
pip install -r requirements.txt

# Test that everything is setup correctly.
make test
```

## Check out a new branch and make your changes

```bash
# Checkout a new branch and make your changes
git checkout -b my-new-feature-branch
# Make your changes...
```

## Run tests and linting

Run tests and linting locally to make sure everything is working as expected.

```bash

# Run automated code formatting. Termii-py uses black.
# (https://github.com/ambv/black
make format

# Run linting. Termii-py uses flake8
# (https://github.com/PyCQA/flake8)
make lint

# Test code. Termii-py uses pytest.
# https://github.com/pytest-dev/pytest
make test
```

## Commit and push your changes

Commit your changes, push your branch to GitHub, and create a pull request.

When your pull request is ready for review, add a comment with the message "please review" and I'll take a look as soon as I can.


## Code documentation

When contributing to termii-py, please make sure that all code is well documented. The following should be documented using properly formatted docstrings:

1. Modules
2. Class definitions
3. Function definitions
4. Module-level variables
