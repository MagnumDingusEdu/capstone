from django.urls import path

from .views import (
    dashboard_redirector_view,
    StudentDashboardView,
    StaffDashboardView,
    NoticeBoardView,
    ChangePasswordView,
    ScholarshipListView,
    MCMTietApplicationView,
    MCMAlumniApplicationView,
    MCMOtherApplicationView,
    ApplicationsListView,
    GrievanceSubmitView,
    GrievanceListView,
    AccountSettingsView,
    ScholarshipCalculatorView,
    ReportsView,
    UploadScholarshipsView,
    UploadAccountsView, MyScholarshipsView
)

app_name = "website"

urlpatterns = [
    path("", dashboard_redirector_view, name="landing-page"),
    path(
        "student-dashboard/", StudentDashboardView.as_view(), name="student-dashboard"
    ),
    path("staff-dashboard/", StaffDashboardView.as_view(), name="staff-dashboard"),
    path("notice-board/", NoticeBoardView.as_view(), name="notice-board"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("scholarships/", ScholarshipListView.as_view(), name="scholarship-list"),
    path(
        "scholarships/mcm_tiet/<int:scholarship_id>/apply/",
        MCMTietApplicationView.as_view(),
        name="mcm-tiet-apply",
    ),
    path(
        "scholarships/mcm_alumni/<int:scholarship_id>/apply/",
        MCMAlumniApplicationView.as_view(),
        name="mcm-alumni-apply",
    ),
    path(
        "scholarships/mcm_other/<int:scholarship_id>/apply/",
        MCMOtherApplicationView.as_view(),
        name="mcm-other-apply",
    ),
    path("my-applications/", ApplicationsListView.as_view(), name="applications-list"),
    path(
        "grievance/submit/", GrievanceSubmitView.as_view(), name="grievance-submit-view"
    ),
    path("grievances/", GrievanceListView.as_view(), name="grievance-list-view"),
    path(
        "account/settings/", AccountSettingsView.as_view(), name="account-settings-view"
    ),
    path(
        "scholarship-calculator",
        ScholarshipCalculatorView.as_view(),
        name="scholarship-calculator",
    ),
    path("reports/", ReportsView.as_view(), name="reports"),
    path("upload-scholarship/", UploadScholarshipsView.as_view(), name='upload-scholarship-data'),
    path("upload-account/", UploadAccountsView.as_view(), name='upload-account-data'),
    path("my-scholarships/", MyScholarshipsView.as_view(), name='my-scholarships')
]
