from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class NewForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    location = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=12)
    birthday_date = forms.DateField()

    def save(self, commit=True):
        user = super(NewForm, self).save(False)
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            profile = Profile(location=self.cleaned_data['location'],
                              phone_number=self.cleaned_data['phone_number'],
                              birthday_date=self.cleaned_data['birthday_date'])
            profile.user = user
            profile.save()

        return user
