from django.urls import path
from .views import *
app_name="project"
urlpatterns=[
    path('register/',UserRegistrationviews.as_view(),name="register"),
    path('login/',UserloginView.as_view(),name="login")

]