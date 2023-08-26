from django import forms
from .models import karbar
from .models import homework


class karbarform(forms.ModelForm):
    class Meta:
        model = karbar
        fields = ('name','lastname', 'address','email', 'password','linkclass','phone','cm','profile',)


class homeworkform(forms.ModelForm):
    class Meta:
        model = homework
        fields = ('cm', 'file')