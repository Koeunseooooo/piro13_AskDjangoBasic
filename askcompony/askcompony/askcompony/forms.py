from django import forms
from .models import Item

class ItemForm(forms.Form):
    class Meta:
        model = Item
        fields = '__all__'