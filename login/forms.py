from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
class settings :
    USE_REMEMBER_ME=True
class SignIn(forms.Form):
    password = forms.CharField(label="password",max_length=25)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #if settings.USE_REMEMBER_ME:
        self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)
    

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('You entered an invalid password.'))

        return password

    
class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label="text",max_length=25)

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username).first()
        if not user:
                raise ValidationError(_('You entered an invalid username.'))


        self.user_cache = user

        return username
    