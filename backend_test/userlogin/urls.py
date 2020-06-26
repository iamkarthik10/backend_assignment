from django.urls import path, include
from userlogin import views

urlpatterns = [
    path('', views.get_json, name='get_json')
]