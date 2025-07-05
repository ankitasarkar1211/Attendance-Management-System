from django import forms
from django.core.validators import RegexValidator


class studentLoginForm(forms.Form):
  enrollment=forms.CharField(max_length=14,
    validators=[RegexValidator(r'^\d{1,14}$', message="Enrollment number must be up to 14 digits.")]) #integer field e max char dewa jayna
  password=forms.CharField(widget=forms.PasswordInput)

class teacherLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
