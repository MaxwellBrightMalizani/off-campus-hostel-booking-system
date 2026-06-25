from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Registration form for both students and hostel owners."""

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First name'}),
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'}),
    )
    user_type = forms.ChoiceField(
        choices=CustomUser.UserType.choices,
        widget=forms.RadioSelect,
        initial=CustomUser.UserType.STUDENT,
        label="I am a",
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_type')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']

        # student_id removed from registration UI/backend validation.
        user.student_id = None

        if commit:
            user.save()
        return user



class EmailLoginForm(forms.Form):
    """
    Login form using email + password (not username).
    """
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'autofocus': True,
            'placeholder': 'you@example.com',
        }),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}),
    )
