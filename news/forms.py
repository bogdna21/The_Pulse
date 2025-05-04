from django import forms
from django.contrib.auth import get_user_model



class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by name"}),
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by username"}),
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by title"}),
    )


User = get_user_model()


class EmailVerificationForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Ваша електронна адреса'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувача з таким email не знайдено.")
        return email


class SetNewPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label="Новий пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введіть новий пароль'}),
    )
    new_password2 = forms.CharField(
        label="Підтвердіть пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторіть новий пароль'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають.")
        return cleaned_data
