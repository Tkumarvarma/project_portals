from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Project,ProjectRequest

class UsuserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
    class Meta:
        model = User
        fields = ["username","first_name","last_name","Mobile_Number","Gender"]
        widgets = {
        "username":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"User Name",
            "primary_key":"true",
            }),
        "first_name":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"First Name",
            }),
        "last_name":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"Last Name",
            }),
        "Mobile_Number":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"Mobile Number",
            }),
        "Gender":forms.Select(attrs={
            "class":"form-control my-2",
            }),
        }

class UspForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","Mobile_Number","Gender","City_or_Village","Mandal","District","State","Profile_Image"]
        widgets = {
        "username":forms.TextInput(attrs={
            "class":"form-control my-2",
            "readonly":"true",
            }),
        "first_name":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"First Name",
            }),
        "last_name":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"Last Name",
            }),
        "email":forms.EmailInput(attrs={
            "class":"form-control my-2",
            "placeholder":"Mailid",
            }),
        "Mobile_Number":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"Mobile Number",
            }),
        "Gender":forms.Select(attrs={
            "class":"form-control my-2",
            }),
        "City_or_Village":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"You Currently staying city or village",
            }),
        "Mandal":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"Mandal",
            }),
        "District":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"District",
            }),
        "State":forms.TextInput(attrs={
            "class":"form-control my-2",
            "placeholder":"State",
            }),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'team_lead', 'points', 'category']

class ProjectRequestForm(forms.ModelForm):
    class Meta:
        model = ProjectRequest
        fields = []

