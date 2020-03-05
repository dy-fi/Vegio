from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(label="Food name- from \"Burgers\" to \"Golden Lentil Dal with Cilantro Speckled Basmati\" ", max_length=300)