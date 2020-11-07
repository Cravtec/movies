from django.urls import path

from .views import SuccessMessagedLogoutView, SubmittableLoginView, SubmittablePasswordChangeView, SignUpView

app_name = 'accounts'

urlpatterns = [
    path("login/", SubmittableLoginView.as_view(), name='login'),
    path('logout/', SuccessMessagedLogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
