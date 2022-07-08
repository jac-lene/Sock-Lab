from django import forms
from .models import BasicSock

class SockForm(forms.ModelForm):

    class Meta:
        model = BasicSock
        fields = ('name', 'CC1', 'CC2','CC3','ankle_height','foot_length','foot_stripe','in_progress','completed')