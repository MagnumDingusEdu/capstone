from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from django.core.exceptions import ValidationError

from .models import UserAccount, Student, Session

admin.site.site_header = "Thapar Scholarship Portal"
admin.site.site_title = "Thapar Scholarship Portal"
admin.site.index_title = "Welcome to the Thapar Scholarship Portal"

admin.site.index_template = "admin/custom_index.html"
admin.autodiscover()

admin.site.unregister(Group)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = UserAccount
        fields = ("email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserPasswordChangeForm(AdminPasswordChangeForm):
    def save(self, commit=True):
        password = self.cleaned_data["password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = UserPasswordChangeForm
    list_display = ("email", "first_name", "last_name", "role", "is_active", "is_staff")
    list_filter = ("is_active", "is_superuser", "role")
    fieldsets = (
        (None, {"fields": ("email", "password", "first_name", "last_name")}),
        ("User Type", {"fields": ("role",)}),
        ("Permissions", {"fields": ("is_active", "is_superuser", "is_staff")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role"),
            },
        ),
    )
    ordering = ("email",)
    search_fields = ("email",)

    filter_horizontal = ()


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "student_name",
        "roll_no",
        "branch_code",
        "sex",
    )
    list_filter = (
        "sex",
        "programme",
        "branch_code",
    )
    change_list_template = "admin/student_change_list.html"

    search_fields = (
        "student_name",
        "user__email",
        "father_name",
        "mother_name",
        "roll_no",
    )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("name", "current")
    list_filter = ("current",)
