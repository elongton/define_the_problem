from django import forms
from django.contrib.auth.models import User
# from users_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        password_confirm = all_clean_data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError("MAKE SURE PASSWORDS MATCH!")
