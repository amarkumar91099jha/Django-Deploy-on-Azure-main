# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django_otp.forms import OTPAuthenticationFormMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class CustomUserCreationForm(UserCreationForm):
    ORGANIZATION_CHOICES = [
        ('NGOs', 'NGOs'),
        ('Enterprise', 'Enterprise'),
        ('Educational Institute', 'Educational Institute'),
        ('Volunteer Organization', 'Volunteer Organization'),
        # Add more choices here if needed
    ]
    organization = forms.ChoiceField(choices=ORGANIZATION_CHOICES)

    USER_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Enterpreneur', 'Enterpreneur'),
        ('Employee', 'Employee'),
        ('Ressolv Certified Surveyor', 'Ressolv Certified Surveyor'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'organization', 'user_type', 'linkedin_url', 'password1', 'password2')


class EmailOTPAuthenticationForm(OTPAuthenticationFormMixin, forms.Form):
    otp_device = 'otp_device'
    otp_challenge = 'otp_challenge'
    otp_token = forms.CharField(required=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['otp_token'].label = 'OTP'

    def clean(self):
        self.cleaned_data = super().clean()
        self.cleaned_data[self.otp_device] = self.get_device()
        return self.cleaned_data

    def get_user(self):
        return self.user