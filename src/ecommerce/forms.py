from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        # to check out this in https://docs.djangoproject.com/en/2.1/ref/forms/widgets/#django.forms.TextInput
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder": "Your message"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label = "confirm password", widget=forms.PasswordInput)
    def clean(self):
        data = self.cleaned_data
        password  = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Password not match")
        return data