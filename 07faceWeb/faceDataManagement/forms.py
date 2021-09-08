from django import forms
from .models import Name_Picture


class Form(forms.ModelForm):

    class Meta:
        model = Name_Picture
        fields = (
            'names',
        )
