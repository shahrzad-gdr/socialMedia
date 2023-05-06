from django.urls import path
from account import views as account_view

urlpatterns = [
    path('', account_view.index, name='index'),
    path('login/', account_view.user_login, name='login'),
    path('register/', account_view.user_register, name='register'),
    path('logout/', account_view.user_logout, name='logout'),
]
