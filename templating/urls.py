from django.urls import path
from . import views

app_name = 'templating'

urlpatterns = [
    path('', views.listing, name='listing'),
    path('view/<str:slug>/', views.view, name='view'),
    path('add/', views.add, name='add'),
]
