from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms




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


    