from django.contrib.auth.forms import AdminPasswordChangeForm
from django.forms import ModelForm

from website.models import MCMTietApplication, Grievance


class UserPasswordChangeForm(AdminPasswordChangeForm):
    def save(self, commit=True):
        password = self.cleaned_data['password1']
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class MCMTietApplicationForm(ModelForm):
    class Meta:
        model = MCMTietApplication
        fields = '__all__'

        exclude = ('remarks', 'status')

    def __init__(self, student_id, scholarship_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].value = student_id
        self.fields['student'].initial = student_id
        self.fields['student'].disabled = True
        self.fields['declaration'].required = True
        self.fields['scholarship'].value = scholarship_id
        self.fields['scholarship'].initial = scholarship_id
        self.fields['scholarship'].disabled = True


class GrievanceForm(ModelForm):
    class Meta:
        model = Grievance
        fields = '__all__'
        exclude = ('date_opened', 'resolved', 'remarks')

    def __init__(self, student_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].value = student_id
        self.fields['student'].initial = student_id
        self.fields['student'].disabled = True
