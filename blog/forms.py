from django import forms
from .models import Item
from captcha.fields import ReCaptchaField


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']


def validate_phone_number(value):
    if not value.startswith('+') or not value[1:].isdigit():
        raise forms.ValidationError('Некорректный формат номера телефона.')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField()
