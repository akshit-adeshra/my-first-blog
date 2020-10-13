from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email_id = forms.EmailField()
    