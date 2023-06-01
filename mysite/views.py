from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    def form_valid(self, form):
        # 이메일 인증을 위해 is_active를 False로 설정
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        self.send_email_confirmation(user)
        return super().form_valid(form)

class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.confirm(request)
        # A React Router Route will handle the failure scenario
        return HttpResponseRedirect('/login/success/')

    def get_object(self):
        key = self.kwargs['key']
        email_confirmation = get_object_or_404(EmailConfirmation, key__iexact=key)
        return email_confirmation