from django.urls import path
from notebook_config import views


urlpatterns = [
    path("", views.index, name="index"),
]
