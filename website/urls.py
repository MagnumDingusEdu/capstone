from django.urls import path
from .views import SignUpView, logout_view, SignInView, dashboard_redirector_view, StudentDashboardView, \
    StaffDashboardView

app_name = 'website'

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-up/", SignUpView.as_view(), name="sign-up"),

    path("", dashboard_redirector_view, name="landing-page"),
    path("student-dashboard/", StudentDashboardView.as_view(), name='student-dashboard'),
    path("staff-dashboard/", StaffDashboardView.as_view(), name='staff-dashboard'),

]
