from io import BytesIO

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView
from oauthlib.oauth2.rfc6749.errors import LoginRequired

from accounts.models import UserAccount, Student, Session
from website.forms import UserPasswordChangeForm, MCMTietApplicationForm, GrievanceForm
from website.mixins import StudentRequired, StaffRequired
from website.models import Scholarship, NoticeCategory, ScholarshipCategory, Notice, MCMTietApplication, Grievance, \
    Constraint, ReceivedScholarship
import pandas as pd


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


class ReportsView(StaffRequired, TemplateView):
    template_name = "pages/reports.html"

    def get_context_data(self, **kwargs):
        context = super(ReportsView, self).get_context_data(**kwargs)
        context['user_count'] = Student.objects.all().count()
        context['scholarship_amount'] = ReceivedScholarship.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
        context['scholarship_count'] = ReceivedScholarship.objects.all().count()
        context['scholarship_percentage'] = Student.objects.filter(
            receivedscholarship__isnull=False).count() / Student.objects.all().count() * 100
        context['female_count'] = Student.objects.filter(receivedscholarship__isnull=False, sex="F").count()
        context['male_count'] = Student.objects.filter(receivedscholarship__isnull=False, sex="M").count()
        context['sessions'] = Session.objects.all()
        historical_data = []

        for i, session in enumerate(Session.objects.all().order_by('-name')):
            amount = ReceivedScholarship.objects.filter(session=session).aggregate(Sum('amount'))['amount__sum'] or 0
            historical_data.append({'id': i, 'session': session.name, 'scholarship_amount': amount})

        context['historical_data'] = historical_data
        return context

    def post(self, *args, **kwargs):
        session_id = self.request.POST.get("session")
        session = get_object_or_404(Session, pk=session_id)
        io = BytesIO()
        writer = pd.ExcelWriter(io)

        branches = ReceivedScholarship.objects \
            .order_by('branch').values_list('branch', flat=True).distinct()

        for branch in branches:
            scholarships = ReceivedScholarship.objects.filter(branch=branch, session=session)
            prepped_dataset = []

            for s in scholarships:
                prepped_dataset.append({
                    'Name': s.student.user.first_name + " " + s.student.user.last_name,
                    'Roll No': s.student.roll_no,
                    'E-mail': s.student.user.email,
                    'Received Scholarship': s.scholarship.name,
                    'Scholarship Type': s.scholarship.verbose_type(),
                    'Amount': s.amount,
                    'current_cgpa': s.current_cgpa,
                    'cgpa_1st_semester': s.cgpa_1st_semester,
                    'cgpa_2nd_semester': s.cgpa_2nd_semester,
                    'cgpa_3rd_semester': s.cgpa_3rd_semester,
                    'sgpa_5th_semester': s.sgpa_5th_semester,
                    'sgpa_6th_semester': s.sgpa_6th_semester,
                    'agpa': s.agpa,
                    'marks': s.marks,
                    'jee_rank': s.jee_rank,
                    'pcme_percentage': s.pcme_percentage,
                    'pcb_percentage': s.pcb_percentage,
                    'ti_rank': s.ti_rank,
                    'tu_rank': s.tu_rank,
                    'twelfth_overall_percentage': s.twelfth_overall_percentage,
                })

            df = pd.DataFrame(prepped_dataset)

            df = df.dropna(axis=1, how='all')
            df.to_excel(writer, sheet_name=branch, index=False)
            # Auto-adjust columns' width
            for column in df:
                column_width = max(df[column].astype(str).map(len).max(), len(column)) + 10
                col_idx = df.columns.get_loc(column)
                writer.sheets[branch].set_column(col_idx, col_idx, column_width)

        writer.close()

        resp_file = io.getvalue()
        response = HttpResponse(resp_file, content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename=Scholarship Report {session.name}.xls'
        return response


class NoticeBoardView(StudentRequired, ListView):
    template_name = "pages/notices.html"
    model = NoticeCategory


class ChangePasswordView(LoginRequired, FormView):
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


class MCMTietApplicationView(SuccessMessageMixin, StudentRequired, CreateView):
    model = MCMTietApplication
    form_class = MCMTietApplicationForm

    success_message = 'Your application was submitted successfully.'

    def get_success_url(self):
        return reverse_lazy('website:mcm-tiet-apply', kwargs={'scholarship_id': self.kwargs['scholarship_id']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        scholarship_id = self.kwargs['scholarship_id']
        kwargs['student_id'] = self.request.user.student.id
        kwargs['scholarship_id'] = scholarship_id
        return kwargs

    def get_context_data(self, **kwargs):
        scholarship = get_object_or_404(Scholarship, pk=self.kwargs['scholarship_id'])
        context = super(MCMTietApplicationView, self).get_context_data()
        context['scholarship'] = scholarship
        return context

    template_name = "pages/mcm-tiet-application-form.html"


class ApplicationsListView(StudentRequired, TemplateView):
    template_name = "pages/applications.html"

    def get_context_data(self, **kwargs):
        context = super(ApplicationsListView, self).get_context_data(**kwargs)
        context['mcm_tiet_applications'] = MCMTietApplication.objects.filter(student=self.request.user.student)
        # TODO: Add rest of the applications
        return context

    def post(self, request):
        # TODO: add paramater application_type, switch case based on that
        # Select appropriate model (MCMTietApplication, MCMAlumini etc.) and delete
        return HttpResponse("Failed. Please try again.")
        try:
            application = get_object_or_404(MCMTietApplication, pk=self.request.POST.get("application_id"))
            application.delete()
        except Exception as e:
            messages.error(request, "Failed to withdraw application. Error : " + str(e))
        messages.success(request, "The specified application was successfully withdrawn")
        return redirect(reverse_lazy("website:mcm-tiet-application-list"))


class GrievanceSubmitView(StudentRequired, SuccessMessageMixin, CreateView):
    model = Grievance
    success_message = 'Your grievance was submitted successfully'
    template_name = 'pages/submit-grievance.html'
    form_class = GrievanceForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['student_id'] = self.request.user.student.id
        return kwargs

    def get_success_url(self):
        return reverse_lazy('website:grievance-list-view')


class GrievanceListView(StudentRequired, ListView):
    template_name = "pages/grievance-list.html"
    model = Grievance


class AccountSettingsView(StudentRequired, TemplateView):
    template_name = "pages/account-settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['student'] = self.request.user.student
        return context


class ScholarshipCalculatorView(StudentRequired, TemplateView):
    template_name = "pages/scholarship-calculator.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['constraints'] = Constraint.objects.all()
        return context

    def post(self, request):

        constraint_id_to_value = {}

        for k, v in self.request.POST.dict().items():
            if k == 'csrfmiddlewaretoken':
                continue

            if not v or v == '':
                continue
            constraint_id_to_value[int(k)] = v

        print(constraint_id_to_value)
        answer = []

        for scholarship in Scholarship.objects.all():
            constraints = scholarship.scholarshipconstraint_set.all()

            relevant = True

            for scholarship_constraint in constraints:

                if scholarship_constraint.constraint.id not in constraint_id_to_value.keys():
                    relevant = False
                    break
                submitted_value = float(constraint_id_to_value[scholarship_constraint.constraint.id])
                if scholarship_constraint.min_value:
                    if submitted_value < scholarship_constraint.min_value:
                        relevant = False

                        break
                if scholarship_constraint.max_value:
                    if submitted_value > scholarship_constraint.min_value:
                        relevant = False
                        break
            if relevant:
                answer.append(scholarship)

        return render(self.request, 'pages/relevant-scholarships.html', {'scholarships': answer})
