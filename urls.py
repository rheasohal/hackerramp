from django.urls import path
from finder import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze_webpage/', views.analyze_webpage, name='analyze_webpage'),
]
