from django.urls import path

from . import views

# localhost:8000/users/
urlpatterns = [
    # path("login/", views.login, name="login"),
    path('register/', views.registerPage, name='register')
]