from django import forms
from django.core.validators import RegexValidator
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone_number', 'message']

    phone_regex = r'^\+91\d{10}$'
    phone_number = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                regex=phone_regex,
                message="Phone number must be in the format: '+911234567890' and exactly 13 digits."
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'XXXXXXXXXX'}),
    )
