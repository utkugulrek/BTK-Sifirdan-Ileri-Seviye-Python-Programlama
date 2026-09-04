from django.urls import path
from . import views  # Aynı dizinde olduğu için .

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about")
]