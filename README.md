# Inspiration Board: Back-end Layer

This scaffold includes the following:

## `app/__init__.py`

This file configures the app. We expect developers to modify this file by:
- Importing all models
- Importing `db` and `migrate` from a separate file that manages creating the `SQLAlchemy` and `Migrate` instances
- Initializing the app with the `SQLAlchemy` and `Migrate` instances
- Importing and registering all blueprints

Prior projects like `Solar System` and [`hello-books-api`](https://github.com/AdaGold/hello-books-api) are great resources to reference for project structure and set up needs.

Note that `create_app` also uses CORS. There is no extra action needed to be done with CORS.

## `tests`

This folder only contains an empty `__init__.py` file. Developers are expected to:
- create a `conftest.py` file to set up their app and any necessary test data for testing
- create test files for any model or route tests

## `requirements.txt`

This file lists the dependencies we anticipate are needed for the project.

## `.gitignore`

This is a hidden file which lists specific files and file extension types that should be ignored by the git repo when looking for changed files to stage.
