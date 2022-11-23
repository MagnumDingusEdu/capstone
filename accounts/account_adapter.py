from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from django.shortcuts import redirect

from accounts.models import UserAccount


def email_domain(email):
    return email.split('@')[1]


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if email_domain(user.email) != 'thapar.edu':
            messages.error(request, "Failed to sign in<br>Only @thapar.edu emails are allowed")
            raise ImmediateHttpResponse(redirect('sign-in'))
        if user.id:
            return
        try:
            user = UserAccount.objects.get(email=user.email)
            sociallogin.state['process'] = 'connect'
            perform_login(request, user, 'none')
        except UserAccount.DoesNotExist:
            pass
