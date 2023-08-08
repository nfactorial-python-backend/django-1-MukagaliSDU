from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:first>/add/<int:second>/", views.add, name="add"),
    path("transform/<str:text>/", views.get_uppercase, name="transform"),
    path("check/<str:text>/", views.is_palindrome, name="palindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calc, name="calc")
]