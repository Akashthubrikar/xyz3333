
from django.urls import path
from .views import candidate_list

urlpatterns = [
    path('candidates/', candidate_list, name='candidate-list'),
]
