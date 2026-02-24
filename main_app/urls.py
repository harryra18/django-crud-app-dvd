from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('dvds/', views.DVDList.as_view(), name='dvd-index'),
    path('dvds/create/', views.DVDCreate.as_view(), name='dvd-create'),
    path('dvds/<int:pk>/', views.DVDDetail.as_view(), name='dvd-detail'),
    path('dvds/<int:pk>/update/', views.DVDUpdate.as_view(), name='dvd-update'),
    path('dvds/<int:pk>/delete/', views.DVDDelete.as_view(), name='dvd-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]