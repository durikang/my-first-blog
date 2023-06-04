from django.contrib import admin
from django.urls import path, include,re_path
from django.contrib.auth import views as auth_views
from allauth.account.views import ConfirmEmailView, EmailVerificationSentView
from .views import CustomSignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('account-confirm-email/', EmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('', include('blog.urls')),
]
  