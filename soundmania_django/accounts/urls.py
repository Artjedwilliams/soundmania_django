from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login_page"),
    path("register/", views.register_view, name="register"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "forgot-password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/forgot-password/done/",
        ),
        name="password_reset",
    ),
    path(
        "forgot-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/reset/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
