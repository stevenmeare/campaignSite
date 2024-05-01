from django.urls import path
from user_auth import views

app_name = 'user_auth'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
name='authenticate_user'),
    path('user/', views.show_user, name='show_user'),
    path('signup/', views.signup, name='signup'),
    path('registered/', views.registered, name='registered')
]