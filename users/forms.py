from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from InvGen.models import InviteCodes
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',)

class InviteAuth(forms.Form):
    invite = forms.CharField(max_length=50, required=True,)
    def clean_invite(self):
        data = self.cleaned_data['invite']
        if data != ("meme"):
            raise ValidationError("Wrong")
        return invite
