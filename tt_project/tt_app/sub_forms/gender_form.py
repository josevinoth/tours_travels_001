from django import forms
from ..models import gender_info

class genderaddForm(forms.ModelForm):
    class Meta:
        model = gender_info
        fields = '__all__'

def __init__(self, *args, **kwargs):
    super(genderaddForm, self).__init__(*args, **kwargs)
    self.fields['arc_customer'].empty_label = "--Select--"