
from django import forms
from . models import People
class UserForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('Name', 'Password')
        labels={
            'Name':'名前',
            'Password':'パスワード',
        }