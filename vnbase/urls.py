from django.urls import path
from . import views

app_name = "vnbase"


urlpatterns = [
    path("", views.index, name="index"),
    path("mvn/<str:param>/", views.mvn, name="mvn"),
    path("zfbvn/<str:param>/", views.mvn, name="mvn"),
]
