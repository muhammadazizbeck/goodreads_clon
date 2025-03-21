from . import views
from django.urls import path


app_name = 'users'
urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('profile/update/',views.ProfileUpdateView.as_view(),name='profile-update')
]