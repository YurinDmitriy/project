from django import forms
from .models import Cart


class CartChangeForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["quantity"]

    quantity = forms.IntegerField()
