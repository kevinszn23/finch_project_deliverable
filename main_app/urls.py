from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('birds/', views.BirdsList.as_view(), name="birds_list"),
    path('birds/new/', views.BirdsCreate.as_view(), name="birds_create"),
    path('birds/<int:pk>/', views.BirdsDetail.as_view(), name="birds_detail"),
    path('birds/<int:pk>/update',views.BirdsUpdate.as_view(), name="birds_update"),
    path('birds/<int:pk>/delete',views.BirdsDelete.as_view(), name="birds_delete"),
]
