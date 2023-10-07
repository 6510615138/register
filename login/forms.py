from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

    
class SignInViaUsernameForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=25)
    password = forms.CharField(label=_('Password'), max_length=25, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label=_('Remember me'), required=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is None:
                raise ValidationError(_('Invalid username or password.'))
            elif not user.is_active:
                raise ValidationError(_('This account is inactive.'))
            else:
                self.user_cache = user
                

    def login(self, request):
        if hasattr(self, 'user_cache'):
            login(request, self.user_cache)
            messages.success(request,"login success!")
    
    def logout(self,request):
        logout(request)   
        messages.success(request,"You are loged out!") 

        


    