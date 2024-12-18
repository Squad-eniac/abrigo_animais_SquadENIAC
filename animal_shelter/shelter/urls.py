from django.urls import path
from .views import AnimalListView, AdoptionRequestView, AnimalDetailView

urlpatterns = [
  path('', AnimalListView.as_view(), name='animal_list'),
  path('adoption/<int:animal_id>/', AdoptionRequestView.as_view(), name='adoption_request'),
  path('animal/<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
]