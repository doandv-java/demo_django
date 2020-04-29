from django import forms


class StoreForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.Textarea()
    phone = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=50)
