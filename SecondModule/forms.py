from django import forms
from SecondModule.models import UserData

class UserForm(forms.ModelForm):
    class Meta:
        model=UserData
        fields=['username','password']
        