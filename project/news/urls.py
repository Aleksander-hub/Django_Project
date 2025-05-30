from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.news_detail, name='news_detail')
]
