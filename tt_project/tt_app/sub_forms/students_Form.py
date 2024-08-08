from django import forms
from ..models import students_info

class studentsaddForm(forms.ModelForm):
    class Meta:
        model = students_info
        fields = '__all__'