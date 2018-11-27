from django import forms
from django.forms import TextInput, Select, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'profile_name': TextInput(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
            'area': Select(attrs={'class':'form-control'}),
            'phone': TextInput(attrs={'class':'form-control'}),
            'address': TextInput(attrs={'class':'form-control'}),
            'nid': TextInput(attrs={'class':'form-control'})
        }
