from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address', 'latitude', 'longitude')
        widgets = {
            'address': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput()
            }
