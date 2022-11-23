from django.contrib.auth.forms import AdminPasswordChangeForm


class UserPasswordChangeForm(AdminPasswordChangeForm):
    def save(self, commit=True):
        password = self.cleaned_data['password1']
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
