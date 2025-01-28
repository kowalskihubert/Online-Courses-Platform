from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import ContactMessage, Review


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'star-rating'}),
        label="Twoja ocena"
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Napisz swoją opinię (opcjonalnie)...',
            'class': 'form-textarea'
        }),
        required=False,
        label="Treść opinii"
    )

    class Meta:
        model = Review
        fields = ['rating', 'text']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user and self.user.is_authenticated:
            instance.user = self.user
        if commit:
            instance.save()
        return instance


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'pattern': '[^@]+@[^@]+\.[a-zA-Z]{2,}'})

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'reason', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={
                'required': True,
                'class': 'form-input',
                'placeholder': 'jan.smith@gmail.com'
            }),
            'message': forms.Textarea(attrs={
                'required': True,
                'minlength': 10,
                'class': 'form-textarea',
                'placeholder': 'Proszę opisać swoje zapytanie...',
                'rows': 5
            }),
            'reason': forms.Select(choices=[
                ('support', 'Wsparcie techniczne'),
                ('lesson', 'Zajęcia indywidualne'),
                ('question', 'Zapytanie'),
                ('other', 'Inne')],
                attrs={
                    'required': True,
                    'class': 'form-select'
                }),
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'np. Jan'
            })
        }

        labels = {
            'name': 'Twoje imię (opcjonalnie)',
            'email': 'Twój adres e-mail',
            'reason': 'Powód kontaktu',
            'message': 'Treść wiadomości'
        }

        error_messages = {
            'email': {
                'required': 'Adres email jest wymagany',
                'invalid': 'Podaj prawidłowy adres email'
            }
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nazwa użytkownika",
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    password = forms.CharField(
        label="Hasło",
        widget=forms.PasswordInput(attrs={'class': 'form-input'})
    )