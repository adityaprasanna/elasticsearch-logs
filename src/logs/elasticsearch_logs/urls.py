from django.urls import path
from logs.elasticsearch_logs.api import views

urlpatterns = [
    path("query/", views.Query.as_view()),
]
