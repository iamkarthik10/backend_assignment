from django.urls import path, include

urlpatterns = [
    path('', include('userlogin.urls')),
]