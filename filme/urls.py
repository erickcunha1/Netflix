
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Homepage.as_view()),
    path('filmes/', views.Homefilmes.as_view()),
] 
