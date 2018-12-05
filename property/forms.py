from django import forms
from django.forms import TextInput, Select, Textarea
from .models import AddProperty


class AddProperyForm(forms.ModelForm):
    class Meta:
        model = AddProperty
        fields = '__all__'
        exclude = ('profile',)

        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'detail': Textarea(attrs={'class':'form-control'})
        }
