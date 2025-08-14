from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:code>/', views.redirect_view, name='redirect'),
    path('link/<str:code>/', views.detail, name='detail'),
]
