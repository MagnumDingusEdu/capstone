from django.urls import path
from .views import dashboard_redirector_view, StudentDashboardView, StaffDashboardView, NoticeBoardView, \
    ChangePasswordView

app_name = 'website'

urlpatterns = [

    path("", dashboard_redirector_view, name="landing-page"),
    path("student-dashboard/", StudentDashboardView.as_view(), name='student-dashboard'),
    path("staff-dashboard/", StaffDashboardView.as_view(), name='staff-dashboard'),
    path("notice-board/", NoticeBoardView.as_view(), name='notice-board'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password')
]
