from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Offer


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        submit = Submit('button', 'Создать')
        submit.field_classes = 'btn btn-outline-primary btn-lg btn-block'
        self.helper.add_input(submit)
