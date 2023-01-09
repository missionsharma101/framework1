from django.urls import path
from .views import UserRegistrationviews
app_name="project"
urlpatterns=[
    path('register/',UserRegistrationviews.as_view(),name="register")

]