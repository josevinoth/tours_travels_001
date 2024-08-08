from django import forms
from ..models import marks_info

class marksaddForm(forms.ModelForm):
    class Meta:
        model = marks_info
        fields = '__all__'