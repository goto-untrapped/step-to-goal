from django import forms
from .models import Goal

class GoalForm(forms.Form):
    YourGoal = forms.CharField(max_length=1000)
    #message = forms.CharField(max_length=1000)
    #sender = forms.EmailField()    #フィールドとはデータの種類を表す型のようなもの