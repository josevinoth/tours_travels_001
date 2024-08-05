from django import forms
from ..models import registration_info

class registrationaddForm(forms.ModelForm):
    class Meta:
        model = registration_info
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(registrationaddForm,self).__init__(*args, **kwargs)
    #     self.fields['arc_customer'].empty_label = "--Select--"