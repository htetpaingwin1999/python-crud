from django import forms
from .models import Student, Resource
class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "roll", "city")
        widgets = {
            'name' : forms.TextInput(attrs = {'class': 'form-control'} ),
            'roll' : forms.NumberInput(attrs = {'class': 'form-control'} ),
            'city' : forms.TextInput(attrs = {'class': 'form-control'} )
        }

class AddResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ("name", "brand", "storage", "mother_board", "memory", "budget_year", "others")
        widgets = {
            'name' : forms.TextInput(attrs = {'class': 'form-control'} ),
            'brand' : forms.TextInput(attrs = {'class': 'form-control'} ),
            'storage' : forms.TextInput(attrs = {'class': 'form-control'} ),
            'mother_board' : forms.TextInput(attrs = {'class': 'form-control'} ),
            'memory' : forms.TextInput(attrs = {'class': 'form-control'} ),
            'budget_year' : forms.NumberInput(attrs = {'class': 'form-control'} ),
            'others' : forms.TextInput(attrs = {'class': 'form-control'} ),

        }