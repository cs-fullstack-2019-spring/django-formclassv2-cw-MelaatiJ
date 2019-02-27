from django import forms


# Give it a name, date of birth, position applying to, and salary.
#class Employee application form
class EmployeeApplicationForm(forms.Form):
    name = forms.CharField()
    date_of_birth = forms.DateField()
    position_applying = forms.CharField()
    salary = forms.IntegerField()

