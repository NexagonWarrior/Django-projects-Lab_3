from django import forms
from .models import stud_list

class StudentForm(forms.ModelForm):
    class Meta:
        model = stud_list
        fields = ['name', 'group', 'grade1', 'grade2','grade3', 'grade4', 'grade5', 'scholarship']
