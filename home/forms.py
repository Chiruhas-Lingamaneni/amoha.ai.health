from django import forms
from django.contrib.auth.models import User
from home.models import UserSignupDb,UserImage,UserQuery

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
    
    def clean(self):
        cleaned_data=super(UserForm, self).clean()
        password=cleaned_data.get("password")
        confirm_password=cleaned_data.get("confirm_password")
        print("hai1")
        if password != confirm_password:
            print("hai2")
            self.add_error('confirm_password', "Password does not match")

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserSignupDb
        fields=('mobileNumber','age','gender')

class UserImageForm(forms.ModelForm):
    class Meta():
        model=UserImage
        fields=('patienteye',)

class UserQueryForm(forms.ModelForm):
    class Meta():
        model=UserQuery
        fields=('name','email','mobileNumber','organisation','message',)