# Django review

## 0. Resources

- [Python Django - The Practical Guide](https://udemy.com/course/python-django-the-practical-guide/)

## 1. Introduction

1. Django is Python web dev framework
    1. for Python 3
    2. "Batteries included": offers build-in solutions and features
    3. customizable and extensible

## 2. Setup

1. Create a Django project
    1. `CLI`:`django-admin startproject MY_PROJECT_NAME` it will create a directory called my_project_name
    2. or `CLI`: `django-admin startproject MY_PROJECT_NAME DIRECTORY_PATH` must please create the directory first
2. VS Code Format Document Shortcut
    1. `Shift`+`Alt`+`F`
3. Launch a local development server
    1. `CLI`: `python manage.py runserver`
        1. [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
        2. [localhost:8000](localhost:8000)
4. Create a Django app inside a project
    1. `CLI`: `python manage.py startapp MY_APP_NAME`

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

## 4. URLs/Routes and Views

1. Views
    1. can have functions or classes
    2. for handles requests
    3. editing Views
        1. Views functions
            1. example `my_get_started_project\challenges\views.py`
            2. template

                ```py
                from django.shortcuts import render
                from django.http import HttpResponse

                def FUNCTION_NAME(request):
                    return HttpResponse()
                ```

        2. Create `urls.py` inside the **app** directory
            1. example `my_get_started_project\challenges\urls.py`
            2. template

                ```py
                from django.urls import path
                from . import views

                urlpatterns = [
                    path("APP_RELATIVE_PATH", views.function_name)
                ]
                ```

            3. this call URL config
        3. Editing `urls.py` inside the **project** directory
            1. example `my_get_started_project\urls.py`
            2. template

                ```py
                from django.contrib import admin
                from django.urls import path, include

                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path("APP_NAME/", include("APP_NAME.urls"))
                ]
                ```

2. Dynamic Path Segments
    1. example
        1. `my_get_started_project\challenges\urls.py`
        2. `my_get_started_project\challenges\views.py`
    2. template

        ```py
        urlpatterns = [
            path("<VARIABLE_NAME>", views.function_name)
        ]
        ```

        ```py
        def FUNCTION_NAME(request, VARIABLE_NAME):
            return HttpResponse()
        ```

    3. Path Converters template
        1. if a variable can not convert to specific type, it will try the next path

        ```py
        urlpatterns = [
            path("<VARIABLE_TYPE:VARIABLE_NAME>", views.FUNCTION_NAME)
        ]
        ```

3. Redirects
    1. example `my_get_started_project\challenges\views.py`
    2. template

        ```py
            return HttpResponseRedirect("/APP_NAME/" + APP_RELATIVE_PATH)
        ```

4. Named URLs
    1. example
        1. `my_get_started_project\challenges\urls.py`
        2. `my_get_started_project\challenges\views.py`
    2. template

        ```py
        # \APP_NAME\urls.py

        urlpatterns = [
            path("<VARIABLE_NAME>", views.FUNCTION_NAME, name=PATH_NAME)
        ]
        ```

        ```py
        # \APP_NAME\views.py
        from django.urls import reverse

        PATH = reverse(PATH_NAME, args=[ARG_NAME]) # /PATH_NAME/ARG_NAME
        ```
