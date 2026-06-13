from django.urls import path
from .views import LandingView, HomeView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('playground/', HomeView.as_view(), name='home'),
]