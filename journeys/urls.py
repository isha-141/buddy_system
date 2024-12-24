from django.urls import path
from . import views

urlpatterns = [
    path('journeys/', views.journeys, name='journeys'),
    path('journeys/addRequest/', views.addRequest, name='addRequest'),
    path('journeys/addRequest/saverequest/', views.saverequest, name='saverequest'),
    path('journeys/findBuddy/', views.findBuddy, name='findBuddy'),
]