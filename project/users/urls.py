from django.urls import path

from . import views

# localhost:8000/users/
urlpatterns = [
    # path("login/", views.login, name="login"),
    path('', views.base, name='base'),
    path('register/', views.registerPage, name='register'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("budget/", views.budget, name="budget"),
    path("profile/", views.profile, name="profile")
]