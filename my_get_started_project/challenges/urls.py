from django.urls import path
from . import views

urlpatterns = [
    # # Create `urls.py` inside the **app** directory
    # path("january", views.january)

    path("", views.challenges_index),
    # Dynamic Path Segments
    # Path Converters
    path("<int:month>", views.challenge_of_the_int),
    # if a variable can not convert to specific type, it will try the next path
    path("<str:month>", views.challenge_of_the_month, name="challenge_of_the_month")
]
