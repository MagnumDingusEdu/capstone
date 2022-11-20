from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from accounts.models import UserAccount
from website.mixins import StudentRequired, StaffRequired


@login_required
def dashboard_redirector_view(request):
    if request.user.is_student():
        return redirect("website:student-dashboard")
    elif request.user.is_staff_member:
        return redirect("website:staff-dashboard")
    else:
        return HttpResponse("You do not have permission to access this page.")


class StudentDashboardView(StudentRequired, TemplateView):
    template_name = "pages/student-dashboard.html"


class StaffDashboardView(StaffRequired, TemplateView):
    template_name = "pages/staff-dashboard.html"

