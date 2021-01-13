from django.urls import path
from rango import views

app_name = "rango"

urlpatterns = [
    path('', views.rango_app, name="index"),
    path('about/', views.rango_about, name="about")
    ]
