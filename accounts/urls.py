from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    LogoutView,
)
from django.urls import path
from .views import SignUpView, SignInView, UploadCSVView

password_reset_view = PasswordResetView.as_view(
    template_name="pages/forgot-password.html"
)
password_reset_done_view = PasswordResetDoneView.as_view(
    template_name="pages/forgot-password-done.html"
)
password_reset_confirm_view = PasswordResetConfirmView.as_view(
    template_name="pages/forgot-password-confirm.html"
)
password_reset_complete_view = PasswordResetCompleteView.as_view(
    template_name="pages/forgot-password-complete.html"
)

urlpatterns = [
    path("forgot-password/", password_reset_view, name="password_reset"),
    path("forgot-password/done/", password_reset_done_view, name="password_reset_done"),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        password_reset_confirm_view,
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        password_reset_complete_view,
        name="password_reset_complete",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path("upload_csv/", UploadCSVView.as_view(), name="upload_csv"),
]
