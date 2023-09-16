from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), max_length=254)
    first_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}), max_length=254)
    last_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}), max_length=254)
    
    class Meta:
            model = User
            fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
            
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "Username"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['email'].label = "Email"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
    

        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'class': 'form-control'})

        self.fields['username'].help_text = "Enter your username"
        self.fields['password1'].help_text = "Enter your password"
        self.fields['password2'].help_text = "Confirm your password"
        self.fields['email'].help_text = "Enter your email"
        self.fields['first_name'].help_text = "Enter your first name"
        self.fields['last_name'].help_text = "Enter your last name"


# Add a new record form
class RecordForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True, label="First Name", widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, label="Last Name", widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(max_length=254, required=True, label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    address = forms.CharField(max_length=200, required=True, label="Address", widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    city = forms.CharField(max_length=100, required=True, label="City", widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(max_length=100, required=True, label="State", widget=forms.TextInput(attrs={'placeholder': 'State', 'class': 'form-control'}))
    zipcode = forms.CharField(max_length=10, required=True, label="Zipcode", widget=forms.TextInput(attrs={'placeholder': 'Zipcode', 'class': 'form-control'}))

    class Meta:
        model = Record
        fields = ('first_name', 'last_name', 'email', 'address', 'city', 'state', 'zipcode')
