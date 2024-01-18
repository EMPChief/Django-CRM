from django.urls import path
from .views import add_lead

urlpatterns = [
    path('add-lead/', add_lead, name='add_lead'),
]
