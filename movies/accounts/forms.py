from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.forms import Form, Textarea, CharField
from django import forms

from .models import Profile


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SignUpForm(SubmittableForm, UserCreationForm):
    biography = CharField(
        label='Tell about your life with movies.',
        widget=Textarea,
        min_length=20,
    )

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'password1', 'password2']

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=user)
        profile.save()
        return user


class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass


class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biography']
