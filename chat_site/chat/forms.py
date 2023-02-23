from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.


class NewUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # profile_pic = forms.ImageField()

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']
        # user.user_profile.profile_pic = self.cleaned_data['profile_pic']
        if commit:
            user.save()
        return user
