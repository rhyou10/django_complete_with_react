from django import forms
from .models import Profile

class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zipcode']