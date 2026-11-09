from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('card/<int:id>', views.get_card, name='card'),
    path('search', views.get_card_by_title, name='search'),
    path('create', views.create_card, name='create'),
]