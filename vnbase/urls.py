from django.urls import path
from . import views

app_name = 'vnbase'


urlpatterns = [
    path("", views.index, name="index"),
]