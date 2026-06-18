from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Registration form for both students and hostel owners.
    student_id is conditionally required based on the chosen user_type.
    """

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
    student_id = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. NRC2024001'}),
        help_text="Required if you are registering as a student.",
    )

    class Meta(UserCreationForm.Meta):
        model  = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_type', 'student_id')

    def clean(self):
        cleaned_data = super().clean()
        user_type  = cleaned_data.get('user_type')
        student_id = cleaned_data.get('student_id', '').strip()

        # Students must supply a student ID
        if user_type == CustomUser.UserType.STUDENT and not student_id:
            self.add_error('student_id', "Student ID is required for student accounts.")

        # Owners must NOT supply a student ID — silently clear it
        if user_type == CustomUser.UserType.OWNER:
            cleaned_data['student_id'] = ''

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email     = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']

        if user.user_type == CustomUser.UserType.STUDENT:
            user.student_id = self.cleaned_data.get('student_id') or None
        else:
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
