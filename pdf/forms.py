from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Profile

class RegistrationForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}), max_length=100, required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"Enter Your Email Address"}),required=True)

    phone = forms.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], widget=forms.NumberInput(attrs={'placeholder': 'Enter Whatsapp Mobile Number'}),required=True)

    address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter Your Address"}), max_length=2000, required=True)

    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your City"}), max_length=100, required=True)

    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your Country"}), max_length=100, required=True)

    summary = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter Your Summary"}), max_length=2000, required=True)    

    degree = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your Degree"}), max_length=100, required=True)

    school = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your School"}), max_length=100, required=True)

    university = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your University"}), max_length=100, required=True)

    previous_work = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter Your Previous Work"}), max_length=2000, required=True)

    skills = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter Your Skills"}), max_length=2000, required=True)


    