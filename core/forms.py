from django.core.mail import send_mail, get_connection

from django import forms
from django.forms.widgets import TextInput



class ContactForm(forms.Form):
    name = forms.CharField(label='sr-only', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your full name *', 'class': 'form-control', 'id': 'form_name'}))

    email = forms.EmailField(label='sr-only', widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email *', 'class': 'form-control', 'id': 'form_email'}),
        required=False)

    message = forms.CharField(label='sr-only', widget=forms.Textarea(
        attrs={'placeholder': 'Your Message *', 'class': 'form-control', 'rows': '4', 'id': 'form_message'}))
