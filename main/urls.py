from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.home, name='home'),
    path("categories/", views.categories, name='categories'),
    path("categories/<pk>", views.books, name='Books'),
    path("register/", views.register, name='register'),
    path("logout/", views.logout_account, name='logout'),
    path("login/", views.login_account, name='login'),
    path("order/<book_pk>", views.order, name='order'),
    path("profile/", views.profile, name='profile'),
    path("giveBack/<order_pk>", views.give_back, name='giveBack')
]
