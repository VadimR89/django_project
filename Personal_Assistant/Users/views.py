from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='News:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='News:main')
        else:
            return render(request, 'signup.html', context={"form": form})

    return render(request, 'signup.html', context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='News:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='login')

        login(request, user)
        return redirect(to='News:main')

    return render(request, 'login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='News:main')


@login_required
def profile(request):
    profile_instance, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile_instance
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect(to="users:profile")

    profile_form = ProfileForm(instance=profile_instance)
    return render(request, "profile.html", {"profile_form": profile_form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'
