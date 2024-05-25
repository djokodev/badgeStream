from django.urls import path
from django.contrib.auth import views as auth_views
from AuthUserManager.views import SignUpView, SignInView

urlpatterns = [
    path('', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]