from django.urls import path
from .views import register, account_activation_sent, activate, user_login, user_logout

urlpatterns = [
    # path('',home,name='home-view'),
    path('register/', register, name='register'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
