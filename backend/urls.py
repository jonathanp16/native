from django.urls import include, path
from rest_framework import routers
import backend.views as views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('test', views.ListUsers.as_view()),
]