from django import forms
from ..models import students_info

class studentsaddForm(forms.ModelForm):
    class Meta:
        model = students_info
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(studentsaddForm, self).__init__(*args, **kwargs)
        self.fields['stu_name'].empty_label = "--Select--"