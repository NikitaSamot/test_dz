from django import forms
from .models import Feedback


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'email', 'message')
