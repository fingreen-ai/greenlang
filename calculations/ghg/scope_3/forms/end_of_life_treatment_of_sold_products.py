""" EndOfLifeTreatment form """
from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.layout import Column, Field

from ...base.forms import PredefinedFactorCalculationMethodForm


class EndOfLifeTreatmentForm(PredefinedFactorCalculationMethodForm):
    """EndOfLifeTreatment form """

    sold_quantity = forms.IntegerField(required=True)

    def get_extra_fields(self):
        return {
            Column(
                Field(
                    'sold_quantity',
                    placeholder=_("Sold quantity"),
                    min=0,
                    type="number",
                    autocomplete="off",
                    css_class="form-control form-control-lg mb-3 mb-lg-0",
                ),
                css_class="col-2",
            ),
        }

    def save(self, commit=True):
        """Save form"""

        instance = super().save(commit=False)

        instance.widget_data = {
            'sold_quantity': self.cleaned_data["sold_quantity"],
        }

        if commit:
            instance.save()

        return instance
    

