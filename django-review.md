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
            2. syntax

                ```py
                from django.shortcuts import render
                from django.http import HttpResponse

                def FUNCTION_NAME(request):
                    return HttpResponse()
                ```

        2. Create `urls.py` inside the **app** directory
            1. example `my_get_started_project\challenges\urls.py`
            2. syntax

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
    2. syntax

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
    2. syntax

        ```py
            return HttpResponseRedirect("/APP_NAME/" + APP_RELATIVE_PATH)
        ```

4. Named URLs
    1. example
        1. `my_get_started_project\challenges\urls.py`
        2. `my_get_started_project\challenges\views.py`
    2. syntax

        ```py
        # \APP_NAME\urls.py

        urlpatterns = [
            path("<VARIABLE_NAME>", views.FUNCTION_NAME, name=PATH_NAME)
        ]
        ```

        ```py
        # \APP_NAME\views.py
        from django.urls import reverse

        PATH = reverse("PATH_NAME", args=[ARG_NAME]) # /PATH_NAME/ARG_NAME
        # or
        PATH = reverse(FUNCTION_NAME, args=[ARG_NAME])
        ```

## 5. Templates

1. HTML files: add to `MY_APP\templates\MY_APP_NAME\`
    1. add `\MY_APP_NAME\` folder is best practice to avoid conflicts across apps
2. Response template string in `views.py`
    1. example `templates_and_static_files\challenges\views.py`
    2. syntax

    ```py
    from django.template.loader import render_to_string
    def FUNCTION_NAME(request, VARIABLE_NAME):
        response = render_to_string("MY_APP_NAME\MY_APP_HTML.html")
        return HttpResponse(response)

    # or
    from django.shortcuts import render
    def FUNCTION_NAME(request, VARIABLE_NAME):
        return render(request, "MY_APP_NAME\MY_APP_HTML.html")

    ```

3. Add template folder manually
    1. `MY_PROJECT\setting.py`

        ```py
        TEMPLATES = [
            {
                'BACKEND': ...,
                'DIRS': [
                    BASE_DIR / "MY_APP" / "templates"
                ],
                'APP_DIRS': True,
                'OPTIONS': ...,
                },
            },
        ]
        ```

4. Add template folder automatically
    1. Set `APP_DIRS': True,` at `MY_PROJECT\setting.py`
    2. See app name at `MY_APP\app.py`
    3. Register app at `MY_PROJECT\setting.py`

        ```py
        INSTALLED_APPS = [
            'MY_APP',
            'django.contrib.admin',
            ...,
        ]
        ```

5. Django Template Language
    1. enhanced HTML to create dynamic pages
    2. example
        1. `templates_and_static_files\challenges\views.py`
        2. `templates_and_static_files\challenges\templates\challenges\challenge.html`
    3. syntax

        ```py
        # in `views.py`
        render(request, "MY_APP_NAME\MY_APP_HTML.html", {
            "KEY":"VALUE"
        }
        ```

        ```html
        <!-- in a `TEMPLATE.html` -->
        {{ VARIABLE_KEY }}
        {}
        ```

6. Filters and Tags
    1. [Built-in filters](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#built-in-filter-reference)
        1. example `templates_and_static_files\challenges\templates\challenges\challenge.html`
        2. syntax `{{ VARIABLE_KEY|FILTER_NAME}}`
    2. [Built-in tags](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#built-in-tag-reference)
        1. example
            1. `templates_and_static_files\challenges\templates\challenges\index.html`
            2. `templates_and_static_files\challenges\templates\challenges\challenge.html`
        2. syntax `{% TAG %}`
        3. commonly use tag

            ```html
            <!-- in a `TEMPLATE.html` -->
            <!-- for loop -->
            {% for NAME in ITERABLE %}
            <!-- ITERABLE is from views.py -->
            <!-- use NAME inside this block -->
                ...
            {% endfor %}

            <!-- Dynamic URLs -->
            {% url "PATH_NAME" ARGUMENT_NAME=VARIABLE_NAME %}

            <!-- if -->
            {% if CONDITION %}
                ...
            {% elif CONDITION %}
                ...
            {% else %}
                ...
            {% endif %}
            ```

    3. Accessing Dictionaries or calling Functions in a template

        ```html
        {{ DICTIONARY.KEY }}
        {{ FUNCTION_NAME }}
        <!--  You cannot call a function that requires arguments in a template -->
        ```

7. Template Inheritance with Tags
    1. Template Inheritance
        1. example
            1. `templates_and_static_files\templates\base.html`
            2. `templates_and_static_files\challenges\templates\challenges\index.html`
            3. `templates_and_static_files\challenges\templates\challenges\challenge.html`
        2. Remember to add parent templates folder path in `MY_PROJECT\setting.py`

            ```py
            TEMPLATES = [{
                ...,
                'DIRS': [
                    BASE_DIR / "templates"
                ],
            }]
            ```

        3. syntax

            ```html
            <!-- in a `PARENT_TEMPLATE.html` -->
            {% block BLOCK_NAME %}DEFAULT CONTENT{% endblock  %}
            ```

            ```html
            <!-- in a `CHILD_TEMPLATE.html` -->
            {% extends "PARENT_TEMPLATE.html" %}
            {% block BLOCK_NAME %}NEW CONTENT{% endblock  %}
            ```

    2. Template Snippets
        1. example
            1. `templates_and_static_files\challenges\templates\challenges\includes`
            2. `templates_and_static_files\challenges\templates\challenges\index.html`
            3. `templates_and_static_files\challenges\templates\challenges\challenge.html`
        2. syntax

            ```html
            <!-- in a `TEMPLATE.html` -->
            {% include "MY_APP_NAME\INCLUDES\SNIPPET_TEMPLATE.html" %}
            <!-- add variables only work in Snippets -->
            {% include "MY_APP_NAME\INCLUDES\SNIPPET_TEMPLATE.html" with VARIABLE_NAME=VALUE %}
            ```

        3. Snippets can access every variable in the template
    3. 404 Template
        1. example
            1. `templates_and_static_files\templates\404.html`
            2. `templates_and_static_files\challenges\views.py`
        2. syntax

            ```py
            from django.http import Http404
            raise Http404()
            # This will automatically return the 404.html when deploy
            ```

## 5. Static Files

1. Static files
    1. for an APP: add to `MY_APP\static\MY_APP_NAME\`
    2. add `\MY_APP_NAME\` folder is best practice to avoid conflicts across apps
    3. CSS, Javascript, picture, etc.
    4. for whole project: add to `MY_PROJECT\static\`
2. Make sure django can load static file
    1. in `MY_PROJECT\setting.py`, make sure

        ```py
        INSTALLED_APPS = [
            ...,
            'django.contrib.staticfiles',
            ...,
        ]
        ```

    2. let Django know where to look for the static files in project level, in `MY_PROJECT\setting.py` add

        ```py
        STATICFILES_DIRS = [
            BASE_DIR / "static"
        ]
        ```

3. Add static files in a template
    1. example
        1. `templates_and_static_files\templates\base.html`
        2. `templates_and_static_files\challenges\static\challenges\challenges.css`
        3. `templates_and_static_files\challenges\templates\challenges\index.html`
    2. syntax

        ```html
        <!-- in a `CHILD_TEMPLATE.html` -->
        {% extends "PARENT_TEMPLATE.html" %}
        {% load static %}
        {% block BLOCK_NAME %}
            <link rel="stylesheet" href="{% static 'MY_APP_NAME\MY_APP_CSS.css' %}">
        {% endblock  %}
        ```

    3. You may have to restart the server to apply the css file
