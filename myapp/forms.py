from django import forms
from .models import Goal

class GoalForm(forms.Form):
    model = Goal        #フォームのフィールドとモデルのフィールドが関連付けられ、フォームから入力されたデータが適切なモデルに保存される
    fields = ['name','content']
    name = forms.CharField(max_length=1000)
    content = forms.CharField(max_length=1000)
        #フィールドとはデータの種類を表す型のようなもの

class ListForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name','content']
        widgets = {  # フォームのウィジェットをカスタマイズします
            'name': forms.TextInput(attrs={'readonly': True}),  # nameフィールドを読み取り専用にします
            'content': forms.TextInput(attrs={'readonly': True}),  # contentフィールドを読み取り専用にします
        }