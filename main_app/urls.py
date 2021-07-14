from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('drummers/', views.drummers_index, name="index"),
    path("drummers/<int:drummer_id>", views.drummers_detail, name="detail"),
    path("drummers/create/", views.DrummerCreate.as_view(), name="drummers_create"),
    path("drummers/<int:pk>/update", views.DrummerUpdate.as_view(), name="drummers_update"),
    path("drummers/<int:pk>/delete", views.DrummerDelete.as_view(), name="drummers_delete"),
    path("drummers/<int:drummer_id>/add_sponsor/", views.add_sponsor, name="add_sponsor"),

]