# Django review

## 0. Resources

- [Python Django - The Practical Guide](https://gale.udemy.com/course/python-django-the-practical-guide/)

## 1. Introduction

1. Django is Python web dev framework
    1. for Python 3
    2. "Batteries included": offers build-in solutions and features
    3. customizable and extensible

## 2. Setup

1. Create a Django project
    1. `CLI`:`django-admin startproject my_project_name` it will create a directory called my_project_name
    2. or `CLI`: `django-admin startproject my_project_name directory_path` must please create the directory first
2. VS Code Format Document Shortcut
    1. `Shift`+`Alt`+`F`
3. Launch a local development server
    1. `CLI`: `python manage.py runserver`
        1. [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
        2. [localhost:8000](localhost:8000)
4. Create a Django app inside a project
    1. `CLI`: `python manage.py startapp my_app_name`

## 3. Django structure

1. Django structure
    1. `manage.py` Django's command-line utility
    2. my_project directory
        1. `asgi.py`, `wsgi.py` important when deployed
        2. `setting.py` project global setting
        3. `urls.py` project pages URL configuration
2. Django App structure
    1. migrations directory: for database and models
    2. `admin.py` for admin
    3. `apps.py` for app setting
    4. `models.py` for database and models
    5. `test.py` for testing
    6. `views.py` for what user see
