from django.urls import path
from .views import candidate_list,web_view

urlpatterns = [
    path('candidates/', candidate_list, name='candidate-list'),
    path('app/<int:id>',web_view)
]
