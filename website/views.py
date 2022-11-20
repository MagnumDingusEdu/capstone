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


class SignInView(TemplateView):
    template_name = "pages/sign-in.html"

    def post(self, request, **kwargs):
        context = {}
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        remember_me = request.POST.get("remember", "")

        if not email or not password:
            context["errors"] = "Both e-mail and password are required fields"
            return super().render_to_response(context)

        user_account = UserAccount.objects.filter(email=email)
        if user_account.exists() and not user_account.first().is_active:
            context["errors"] = "This user account is temporarily deactivated. Please contact us for further details"
            return super().render_to_response(context)

        user = authenticate(email=email, password=password)
        if not user:
            context["errors"] = "Incorrect e-mail / password"
            return super().render_to_response(context)

        login(self.request, user)

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return redirect("website:landing-page")


class SignUpView(TemplateView):
    template_name = "pages/sign-up.html"

    # @transaction.atomic
    # def post(self, request, **kwargs):
    #     roll_no = request.POST.get("roll_no", "")
    #     first_name = request.POST.get("first_name", "")
    #     last_name = request.POST.get("last_name", "")
    #     address = request.POST.get("address", "")
    #     mobile = request.POST.get("mobile", "")
    #     email = request.POST.get("email", "")
    #     password1 = request.POST.get("password1", "")
    #     password2 = request.POST.get("password2", "")
    #
    #     error = False
    #
    #     if not first_name:
    #         messages.error(request, "First Name is required")
    #         error = True
    #     if not last_name:
    #         messages.error(request, "Last Name is required")
    #         error = True
    #     if not email:
    #         messages.error(request, "E-mail is required")
    #         error = True
    #     if not password1 or not password2:
    #         messages.error(request, "Both passwords are required")
    #         error = True
    #
    #     if password1 != password2:
    #         messages.error(request, "Passwords do not match")
    #         error = True
    #
    #     if UserAccount.objects.filter(email=email).exists():
    #         messages.error(request, "This e-mail address is already registered")
    #         error = True
    #
    #     if error:
    #         return super().render_to_response({})
    #     else:
    #         try:
    #             user = UserAccount.objects.create_user(email=email, password=password1)
    #             user.first_name = first_name
    #             user.last_name = last_name
    #             user.save()
    #             Customer.objects.create(user=user, address=address, mobile=mobile)
    #             messages.success(request, "Registered successfully! Please log in now")
    #             return redirect("website:sign-in")
    #         except Exception as e:
    #             messages.error(request, "An error occurred while signing up : " + str(e))
    #     return super().render_to_response({})


class StudentDashboardView(StudentRequired, TemplateView):
    template_name = "pages/student-dashboard.html"


class StaffDashboardView(StaffRequired, TemplateView):
    template_name = "pages/staff-dashboard.html"


def logout_view(request):
    logout(request)
    return redirect('website:sign-in')
