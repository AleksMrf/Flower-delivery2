from django import forms
from catalog.models import Flower

class OrderForm(forms.Form):
    flowers = forms.ModelMultipleChoiceField(
        queryset=Flower.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Выберите цветы"
    )