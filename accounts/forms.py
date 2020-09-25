from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Contact, Client
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm

# class ClientModelForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         exclude = ['user']

class ContactModelForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']