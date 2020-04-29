from django import forms

from .models import Person


# Form of Person
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name']
