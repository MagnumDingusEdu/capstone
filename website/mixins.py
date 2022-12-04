from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

from accounts.models import UserAccount


class StudentRequired(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == UserAccount.STUDENT

    def handle_no_permission(self):
        messages.error(
            self.request,
            "This page can only be accessed by students. Please log in with your e-mail to continue",
        )
        return redirect("sign-in")


class StaffRequired(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == UserAccount.STAFF

    def handle_no_permission(self):
        messages.error(
            self.request,
            "This page can only be accessed by staff members. Please log in with an appropriate account to "
            "continue",
        )
        return redirect("sign-in")
