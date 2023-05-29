from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']


def validate_phone_number(value):
    if not value.startswith('+') or not value[1:].isdigit():
        raise forms.ValidationError('Некорректный формат номера телефона.')


class ContactForm(forms.Form):
    phone_number = forms.CharField(validators=[validate_phone_number])
