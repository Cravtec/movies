from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import (SubmittableAuthenticationForm,
                    SubmittablePasswordChangeForm,
                    SignUpForm,
                    UserUpdateForm,
                    ProfileUpdateForm
                    )


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class = SubmittablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class SuccessMessagedLogoutView(LogoutView):
    success_url = reverse_lazy('index')
    template_name = 'accounts/logout.html'

    def get_next_page(self):
        result = super().get_next_page()
        messages.success(self.request, 'Successfully logged out!')
        return result


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)
