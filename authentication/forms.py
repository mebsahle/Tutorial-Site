from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

class UserRegisterForm(forms.ModelForm):
    user_password = forms.CharField(
        max_length=1024,
        widget=forms.PasswordInput(),
        help_text='password must be at least 8 character',
        label='Password',
    )
    confirm_password = forms.CharField(
        max_length=1024,
        widget=forms.PasswordInput(),
        help_text='*Confirm password'
    )
    class Meta:
        model = User
        fields = ['username', 'email','user_password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        user_password = cleaned_data.get('user_password')
        confirm = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')
        #date_of_birth = cleaned_data.get('date_of_birth')

        if (not username) or (not email) or (not user_password) or (not confirm):
            raise forms.ValidationError("Please correct the errors below.")

        if user_password and confirm:
            if user_password != confirm:
                raise forms.ValidationError("Password is not confirmed.")

        return cleaned_data

class EditUserProfile(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password', 'is_admin', 'is_active',]
        widgets = {
            'registration_date':forms.DateInput(attrs={'readonly':True}),
        }
    
    def clean(self):
        cleaned_data = super.clean()
        username = cleaned_data('username')
        email = cleaned_data('email')
        if (not username) or (not email):
            raise forms.ValidationError("Please correct the errors below.")
        
        return cleaned_data

class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', ]

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if (not username):
            raise forms.ValidationError("Please correct the errors below.")

        return cleaned_data

class EditMyProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if (not username) or (not email):
            raise forms.ValidationError("Please correct the errors below.")
        return cleaned_data

class ChangePassword(forms.Form):
    def __init__(self, *args, **kwargs):
        self.password = kwargs.pop('password', None)
        super(ChangePassword, self).__init__(*args, **kwargs)
    
    old_password = forms.CharField(
        max_length=1024,
        widget=forms.PasswordInput(),
    )
    new_password = forms.CharField(
        label='New Password:',
        max_length=1024,
        widget=forms.PasswordInput(),
        help_text='minimum 8 character'
    )
    confirm = forms.CharField(
        label='New password confirmation:',
        max_length=1024,
        widget=forms.PasswordInput(),
    )

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm')

        if (not old_password) or (not new_password) or (not confirm_password):
            raise forms.ValidationError('Please correct the errors below.')

        if check_password(old_password, self.password):
            if new_password:
                if new_password == confirm_password:
                    return
                else:
                    raise forms.ValidationError("Password is not confirmed")
        else:
            raise forms.ValidationError('Your old password was entered incorrectly. Please enter again.')

        return cleaned_data