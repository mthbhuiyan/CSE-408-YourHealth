from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
