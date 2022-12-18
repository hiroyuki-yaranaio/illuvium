
from django import forms
from . models import People
class UserForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('Name', 'Mail','RegistrationDate')
        labels={
            'Name':'名前',
            'Mail':'メール',
            'RegistrationDate':'登録日',
        }