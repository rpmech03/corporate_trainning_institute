from pyexpat import model
from django import forms
from .models import Student
class DateInput(forms.DateInput):
    input_type = 'date'
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['username','first_name','last_name','email','password','mobile','join_date',
        'total_fees','module','status','image','joining_location']
        widgets = {
            'join_date': DateInput()
        }