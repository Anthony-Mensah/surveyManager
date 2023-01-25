from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('<slug:slug>/', views.answer, name='answer'),
    path('choice/<slug:slug>/', views.choice, name='choice'),
    path('edit/<slug:slug>/', views.edit, name='edit')
]
