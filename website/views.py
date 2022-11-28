from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView
from accounts.models import UserAccount
from website.forms import UserPasswordChangeForm, MCMApplicationForm
from website.mixins import StudentRequired, StaffRequired
from website.models import Scholarship, NoticeCategory, ScholarshipCategory, Notice, MCMApplication


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['notices'] = Notice.objects.all().order_by('-date')[:10]
        return context


class StaffDashboardView(StaffRequired, TemplateView):
    template_name = "pages/staff-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user_count'] = UserAccount.objects.filter(role=UserAccount.STUDENT).count()
        context['scholarships'] = Scholarship.objects.all()
        return context


class NoticeBoardView(StudentRequired, ListView):
    template_name = "pages/notices.html"
    model = NoticeCategory


class ChangePasswordView(StudentRequired, FormView):
    template_name = 'pages/change-password.html'
    form_class = UserPasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, self.request.user)
        messages.success(self.request, "Password has been changed successfully.")
        return redirect('website:change-password')


class ScholarshipListView(StudentRequired, ListView):
    template_name = "pages/scholarship-list.html"
    model = ScholarshipCategory


class MCMScholarshipApplyView(SuccessMessageMixin, StudentRequired, CreateView):
    model = MCMApplication
    form_class = MCMApplicationForm

    success_message = 'Your application was submitted successfully.'

    def get_success_url(self):
        return reverse_lazy('website:mcm-scholarship-apply', kwargs={'scholarship_id': self.kwargs['scholarship_id']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        scholarship_id = self.kwargs['scholarship_id']
        kwargs['student_id'] = self.request.user.student.id
        kwargs['scholarship_id'] = scholarship_id
        return kwargs

    def get_context_data(self, **kwargs):
        scholarship = get_object_or_404(Scholarship, pk=self.kwargs['scholarship_id'])
        context = super(MCMScholarshipApplyView, self).get_context_data()
        context['scholarship'] = scholarship
        return context

    template_name = "pages/mcm-application-form.html"
