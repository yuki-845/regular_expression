from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        labels = {'name': '名前', 'age': '年齢','zip_zode': 'Zip Code', 'tel': 'Tel Phone'}