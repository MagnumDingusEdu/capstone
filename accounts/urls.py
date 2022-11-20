from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, \
    PasswordResetConfirmView
from django.urls import path

password_reset_view = PasswordResetView.as_view(template_name="pages/forgot-password.html")
password_reset_done_view = PasswordResetDoneView.as_view(template_name="pages/forgot-password-done.html")
password_reset_confirm_view = PasswordResetConfirmView.as_view(template_name="pages/forgot-password-confirm.html")
password_reset_complete_view = PasswordResetCompleteView.as_view(template_name="pages/forgot-password-complete.html")

urlpatterns = [
    path('forgot-password/', password_reset_view, name='password_reset'),
    path('forgot-password/done/', password_reset_done_view, name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('password-reset-complete/', password_reset_complete_view, name='password_reset_complete'),
]
