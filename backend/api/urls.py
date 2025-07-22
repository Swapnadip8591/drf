from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home, name='api-home'),   #localhost:8000/api/
]
