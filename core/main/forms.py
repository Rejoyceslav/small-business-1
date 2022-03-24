from django import forms
from .models import Materialy
from django.forms import ModelForm
from django import forms
from .models import Email

from django.utils.translation import gettext_lazy as _


class SendEmailForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({})
        self.fields['company'].widget.attrs.update({})
        self.fields['email'].widget.attrs.update({})
        self.fields['phone'].widget.attrs.update({})
        self.fields['message'].widget.attrs.update({})

        # self.fields['email'] = forms.EmailField(
        #     widget=forms.EmailInput(attrs={
        #         'autocomplete': 'off',
        #         'class': 'subpage_kontakt_form_field',
        #         'placeholder': 'pole wymagane',
        #         'required': 'required'
        #     }),
        #     error_messages={'invalid': 'your custom error message'}
        # )

    class Meta:
        model = Email
        localized_fields = '__all__'
        fields = ['name', 'company', 'email', 'phone', 'message']
        widgets = {  # styling tutaj działa, powyżej w attrs.update({}) nie działa
            'name': forms.TextInput(attrs={'class': 'subpage_kontakt_form_field', 'placeholder': 'pole wymagane'}),
            'company': forms.TextInput(attrs={'class': 'subpage_kontakt_form_field', 'placeholder': 'pole wymagane'}),
            'email': forms.EmailInput(attrs={'class': 'subpage_kontakt_form_field', 'placeholder': 'pole wymagane'}),
            'phone': forms.TextInput(attrs={'class': 'subpage_kontakt_form_field', 'placeholder': 'pole wymagane'}),
            'message': forms.Textarea(attrs={'class': 'subpage_kontakt_message_textarea', 'placeholder': 'pole wymagane'}),
        }

