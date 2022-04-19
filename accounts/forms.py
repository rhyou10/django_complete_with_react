from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zipcode']



class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text= '3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        if answer !=6:
            raise forms.ValidationError('떙')
        return answer
    pass