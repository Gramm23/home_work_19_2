from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact')
]
