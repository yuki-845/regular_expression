from django.urls import path

from . import views
app_name = "regex_app"

urlpatterns = [
    path("", views.confirm, name="confirm"),
]
