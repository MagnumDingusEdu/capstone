from django.urls import path
from .views import dashboard_redirector_view, StudentDashboardView, StaffDashboardView, NoticeBoardView, \
    ChangePasswordView, ScholarshipListView, MCMTietApplicationView, ApplicationsListView, GrievanceSubmitView, \
    GrievanceListView, AccountSettingsView, ScholarshipCalculatorView

app_name = 'website'

urlpatterns = [

    path("", dashboard_redirector_view, name="landing-page"),
    path("student-dashboard/", StudentDashboardView.as_view(), name='student-dashboard'),
    path("staff-dashboard/", StaffDashboardView.as_view(), name='staff-dashboard'),
    path("notice-board/", NoticeBoardView.as_view(), name='notice-board'),
    path("change-password/", ChangePasswordView.as_view(), name='change-password'),
    path("scholarships/", ScholarshipListView.as_view(), name='scholarship-list'),
    path("scholarships/mcm_tiet/<int:scholarship_id>/apply/", MCMTietApplicationView.as_view(),
         name='mcm-tiet-apply'),
    path("my-applications/", ApplicationsListView.as_view(), name='applications-list'),
    path("grievance/submit/", GrievanceSubmitView.as_view(), name='grievance-submit-view'),
    path("grievances/", GrievanceListView.as_view(), name='grievance-list-view'),
    path("account/settings/", AccountSettingsView.as_view(), name='account-settings-view'),
    path("scholarship-calculator", ScholarshipCalculatorView.as_view(), name='scholarship-calculator')
]
