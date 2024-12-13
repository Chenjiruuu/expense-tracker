from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('tracker.urls')),
    path('add/', views.add_expense, name='add_expense'),
    
]