from django.urls import path
from .views import register, custom_login, custom_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', custom_logout, name='logout'),
    path('login/', custom_login, name='login'),
]
